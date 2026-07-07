import os
from setuptools import setup
from setuptools.extension import Extension
from Cython.Build import cythonize

core_dir = "core"
extensions = []

for root, _, files in os.walk(core_dir):
    for file in files:
        if file.endswith(".py") and file != "__init__.py":
            file_path = os.path.join(root, file)
            # Create a module name based on path (e.g., core.utils)
            module_name = file_path.replace(os.sep, ".").rstrip(".py")
            extensions.append(Extension(module_name, [file_path]))

setup(
    name="compiled_core",
    ext_modules=cythonize(
        extensions, 
        compiler_directives={'language_level': "3"},
        exclude_failures=True
    ),
)
