# There are three ways to import a module.

# import -> fetch a module as a whole
# from module import -> fetch selected names from module
# imp.reload() -> reload a module without stopping python interpreter

# Why use modules?

# Code reuse
# Namespace partitioning
# Shared service and data

# How imports work
# Find the module's file.
# Compile it to byte code (if needed).
# Run the module's code to build the objects it defines.

# Where to find modules?

# The home directory of the program
# PYTHONPATH directories (if set)
# Standard library directories
# The contents of any .pth files (if present)
# The site-packages home of third-party extensions

# Module sources

# A source code file
# A byte code file
# An optimized byte code file named *.pyo (a less common format)
# A directory, for package imports
# A compiled extension module, coded in C, C++, or another language, and dynamically
# linked when imported (e.g., *.so on Linux, or *.dll or *.pyd on Cygwin
# and Windows)
# A compiled built-in module coded in C and statically linked into Python
# A ZIP file component that is automatically extracted when imported
# An in-memory image, for frozen executables
# A Java class, in the Jython version of Python
# A .NET component, in the IronPython version of Python

# package import basics

# import dir1.dir2.mod or from dir1.dir2.mod import x
# dir1 and dir2 must contain __init__.py
