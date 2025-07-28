import os
from config import MAX_CHARS

def get_file_content(working_directory, file_path):
    abs_working_directory = os.path.abspath(working_directory)
    target_file = os.path.abspath(os.path.join(abs_working_directory, file_path))

    if not target_file.startswith(abs_working_directory):
        return f"Error: Cannot read '{file_path}' as it is outside the permitted working directory"
    
    if not os.path.isfile(target_file):
        return f"Error: File not found or is not a regular file: '{file_path}'"
    
    with open(file_path, "r") as f:
        file_content_string = f.read(MAX_CHARS)

    print(target_file)