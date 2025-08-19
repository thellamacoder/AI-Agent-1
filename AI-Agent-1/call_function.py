from google.genai import types

from schemas import *

available_functions = types.Tool(
function_declarations=[
schema_get_files_info,
schema_get_file_content,
schema_run_python_file,
schema_write_file,
]
)

def call_function(function_call_part, verbose=False):

    function_name = function_call_part.name
    function_arguments = function_call_part.args
    function_arguments["working_directory"] = "./calculator"

    

    if verbose:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    else:
        print(f" - Calling function: {function_call_part.name}")

    return function_name(**function_arguments)