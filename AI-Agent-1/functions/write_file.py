import os

def write_file(working_directory, file_path, content):
    
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    

    if not abs_file_path.startswith(abs_working_dir):
        return f"Error: Cannot write to '{file_path}' as it is outside the permitted working directory"
    
    # if the file_path does not exist, create it

    try:
        if not os.path.exists(abs_file_path):
            os.makedirs(abs_file_path)
    
    except Exception as e:
        return f"Error: Cannot create path '{abs_file_path}': {e}"
    
    try:
        with open(abs_file_path, "w") as f:
            f.write(content)
    
    except Exception as e:
        return f"Error: cannot write to '{abs_file_path}': {e}" 