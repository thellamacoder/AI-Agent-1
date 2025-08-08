import os
import subprocess

def run_python_file(working_directory, file_path, args=[]):
    
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))

    if not os.path.startswith(abs_working_dir):
        return f"Error: Cannot execute '{file_path}' as it is outside the permitted working directory"
    
    if not os.path.exists(abs_file_path):
        return f"Error: '{file_path}' not found"
    
    file_ext = file_path.split(".")

    if not file_ext == "py":
        return f"Error: '{file_path}' is not a Python file."

    # Use the subprocess.run function to execute the Python file and get back a "completed_process" object.


    """
    Use the subprocess.run function to execute the Python file and get back a "completed_process" object.

    Make sure to:
    - Set a timeout of 30 seconds
    - Capture both stdout and stderr
    - Set the working directory properly
    - Pass along the args if provided
    """

    run_file_result = subprocess.run(executable=abs_file_path, timeout=30, capture_output=True, args=args)

    print(f"STDOUT: {run_file_result.stdout}, STDERR: {run_file_result.stderr}")