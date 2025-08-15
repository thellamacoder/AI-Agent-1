import os
import subprocess

def run_python_file(working_directory, file_path, args=[]):
    
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(abs_working_dir, file_path))

    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.exists(abs_file_path):
        return f'File "{file_path}" not found'
    
    file_ext = file_path.split(".")

    if not file_ext[1] == "py":
        return f"Error: '{file_path}' is not a Python file."

    # Use the subprocess.run function to execute the Python file and get back a "completed_process" object.

    try:
        command_list = ["python"]
        path_list = command_list + [abs_file_path]
        args_list = path_list + args

        run_file_result = subprocess.run(args_list, timeout=30, capture_output=True, text=True, cwd=abs_working_dir)
        if run_file_result.returncode != 0:
            run_file_result.append(f"Process exited with code {run_file_result.returncode}")
        return (f"STDOUT: {run_file_result.stdout} STDERR: {run_file_result.stderr}") if run_file_result else "No output produced."
    
    except Exception as e:
        return f"Error: executing Python file: {e}"