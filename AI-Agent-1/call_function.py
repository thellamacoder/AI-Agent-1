from google.genai import types
from functions.get_file_content import get_file_content
from functions.get_files_info import get_files_info
from functions.run_python import run_python_file
from functions.write_file import write_file
from schemas import *

available_functions = types.Tool(
function_declarations=[
schema_get_files_info,
schema_get_file_content,
schema_run_python_file,
schema_write_file,
]
)

functions_dict = {
    "get_files_info": get_files_info, 
    "get_file_content": get_file_content, 
    "run_python_file": run_python_file, 
    "write_file": write_file,
    }

def call_function(function_call_part, verbose=False):

    function_name = function_call_part.name

    if function_name not in functions_dict:
        return types.Content(
        role="tool",
            parts=[
            types.Part.from_function_response(
                name=function_name,
                response={"error": f"Unknown function: {function_name}"},
            )
        ],
    )
                              
    function_arguments = dict(function_call_part.args or {})
    function_arguments["working_directory"] = "./calculator"

    if verbose:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    else:
        print(f" - Calling function: {function_call_part.name}")

    function = functions_dict[function_name]
    function_result = function(**function_arguments)

    return types.Content(
    role="tool",
    parts=[
        types.Part.from_function_response(
            name=function_name,
            response={"result": function_result},
        )
    ],
)