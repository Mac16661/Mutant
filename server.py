import os
import sys
import json
import argparse
from typing import Annotated
from mcp.server.fastmcp import FastMCP

from groq import Groq
from openai import OpenAI
from dotenv import load_dotenv

# from rich.console import Console
# from rich.markdown import Markdown

from core.genetic_evolution import GeneticEvolutionAlgorithm
from core.logging import logger

# console = Console()
load_dotenv()
########################################  API KEYS  ###############################################
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY")
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
###################################################################################################

########################################  MPC SETUP  ##############################################
parser = argparse.ArgumentParser()
parser.add_argument("--models", default='[{"openai" : "gpt-5.4"}, {"openai": "gpt-5.4"}]')
parser.add_argument("--max_iterations", type=int, default=10)

args = parser.parse_args()
# Debug log
logger.debug(f"Configuring the genetic evolution engine with {args.models} models (max {args.max_iterations} iterations).")
###################################################################################################

################################  EVOLUTION ENGINE SETUP PHASE  ###################################
model_config_list = None
try:
    model_config_list = json.loads(args.models)
    if len(model_config_list) < 2:
        raise "Number of models should be >= 2 " 
except json.JSONDecodeError as e:
    logger.error(f"Error: The provided models argument is not valid JSON. {e}")
    sys.exit(1)

evolution_engine = None 
client = None

for model_config in model_config_list:
    # Per dictionary there will be only one entry
    for cloud, model in model_config.items():   # eg: {"openai" : "gpt-5.4-mini"}
        if cloud == "openai":
            client = OpenAI(api_key = OPENAI_API_KEY)
        elif cloud == "groq":
            client = Groq(api_key = GROQ_API_KEY)
        else:
            logger.error("Error: Client not supported yet")
            raise "Error: Client not supported yet"
            sys.exit(1)

        if evolution_engine == None:
            evolution_engine = GeneticEvolutionAlgorithm(client, model, args.max_iterations)

        evolution_engine.add_node(client, model)

evolution_engine.commit()
###################################################################################################

mcp = FastMCP("Mutant")
@mcp.tool()
def mutant(
    question: Annotated[
        str,
        """INSTRUCTIONS FOR CALLING AI:
        Before executing this tool, you MUST compile a comprehensive, self-contained prompt for the 'question' parameter.
        Do not just forward a shallow user query. You must include:
        1. THE CORE PROBLEM: The exact question or goal.
        2. THE FULL CONTEXT: Any relevant background code, mathematical constraints, system architectures, or medical data from earlier in the conversation.
        3. THE EXPECTED OUTPUT: Explicitly state the format, constraints, and requirements needed for a successful solution.
        
        Ensure the 'question' string contains all information required to solve the problem independently.
        And dont modify the data, just display it as it is."""
    ]
) -> str:
    """
    Mutant uses a genetic evolution algorithm to reduce AI hallucination and improve overall response accuracy at lower cost. It can solve complex maths, science, arts, coding and any logical/reasoning problems much better. Feel free to call this tool when problem is complicated/explicitly mentioned/you are not confident or your answers are incorrect or not satisfactory. 
    """
    logger.debug(question)

    evolution_engine.add_prompt(question)

    converged, raw_results = evolution_engine.run()

    #console.print(Markdown(converged))
    logger.debug(converged)

    evolution_engine.reset()

    return converged

if __name__ == "__main__":
    logger.info("MCP Server started successfully.")
    mcp.run()
