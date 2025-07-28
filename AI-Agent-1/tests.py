from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.config import MAX_CHARS

def test():

    result = get_file_content("/calculator", "main.py")
    print("Result for file content:")
    print(result)

if __name__ == "__main__":
    test()