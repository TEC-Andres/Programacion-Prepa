import ctypes
import os

# Get the absolute path of the current script
script_dir = f'{os.path.dirname(os.path.abspath(__file__))}\\main.dll'

# Load the compiled shared library
nested_lib = ctypes.CDLL(script_dir)  # Use "nested_loops.dll" on Windows

# Run the function
nested_lib.a()
