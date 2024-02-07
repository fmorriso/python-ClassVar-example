import sys
from student import Student
from school import School

def get_python_version() -> str:
	return f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(f"Python version: {get_python_version()}")

    # create Object
    s1 = Student('Emma', 10)
    print(f's1: {s1}')
    s1.show()


    s2 = Student('Vishnu', 11)
    print(f'before s2: {s2}')
    # WARNING: this will create a variable that "shadows" the class variable of the same name
    s2.__school = School('XYZ_School', '9876 E. Main', 1700)
    print(f'after  s2: {s2}')
    print(f'after s2.__school: {s2.__school}')
    s2.show()
