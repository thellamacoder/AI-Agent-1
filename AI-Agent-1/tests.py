from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content

def test():

    result = get_file_content("calculator", "lorem.txt")
    print("Result for calculator/lorem.txt file content:")
    print(result)

    result = get_file_content("calculator", "main.py")
    print("Result for calculator/main.py:")
    print(result)

    result = get_file_content("calculator", "pkg/calculator.py")
    print("Result for calculator/pkg/calculator.py:")
    print(result)

    result = get_file_content("calculator", "/bin/cat")
    print("Result from calculator/bin/cat")
    print(result)

    result = get_file_content("calculator", "pkg/does_not_exist.py")
    print("Result from calculator/pkg/does_not_exixt.py:")
    print(result)
    
if __name__ == "__main__":
    test()