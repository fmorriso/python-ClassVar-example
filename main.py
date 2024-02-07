import sys
from student import Student
def get_python_version() -> str:
	return f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(f"Python version: {get_python_version()}")

    # create Object
    s1 = Student('Emma', 10)
    print('Before')
    s1.show()

