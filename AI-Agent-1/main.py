import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from functions import get_files_info
from prompts import system_prompt
from schemas import *


def main():

    load_dotenv()

    # The line below is equivalent to if "--verbose" in sys.argv: verbose = True else: verbose = False
    verbose = "--verbose" in sys.argv

    # Taken from the boot.dev solution. Not sure how I am supposed to know how to do that from these courses.
    args = []
    for arg in sys.argv[1:]:
        if not arg.startswith("--"):
            args.append(arg)

    if not args:

        print("AI Code Assistant")
        print("\nUsage: python main.py 'your prompt here' [--verbose]")
        print("Example: python main.py 'How do I build a calculator app?'")
        sys.exit(1)

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    user_prompt = " ".join(args)

    if verbose:
        print(f"User prompt: {user_prompt}\n")
    
    messages = [types.Content(role="user", 
        parts=[types.Part(text=user_prompt)]),
    ]

    generate_content(client, messages, verbose)

def generate_content(client, messages, verbose):

    available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
    ]
    )
    
    response = client.models.generate_content(model = "gemini-2.0-flash-001",
        contents = messages, config=types.GenerateContentConfig(tools=[available_functions], system_instruction=system_prompt))
    
    if verbose:
        print(f"Prompt tokens: ", response.usage_metadata.prompt_token_count)
        print(f"Response tokens: ", response.usage_metadata.candidates_token_count)
    
    if not response.function_calls:
        print("Response:")
        print(response.text)

    for function_call_part in response.function_calls:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")



if __name__ == "__main__":
    main()
