from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python import run_python_file

def test():

    result = run_python_file("calculator", "main.py")
    print("/calculator/main.py: should print calculator usage instructions")
    print(result)

    result = run_python_file("calculator", "main.py", ["3 + 5"])
    print("Should print the sum of 3 and 5")
    print(result)

    result = run_python_file("calculator", "tests.py")
    print("Should run the tests.py file inside the calculator directory")
    print(result)

    result = run_python_file("calculator", "../main.py")
    print("Should print an error that the file is outside the working directory")
    print(result)

    result = run_python_file("calculator", "nonexistant.py")
    print("Should print an error that the file doesn't exist")
    print(result)


if __name__ == "__main__":
    test()