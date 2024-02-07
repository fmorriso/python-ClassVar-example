import sys
from student import Student
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
    print(f's2: {s2}')
    # create a variable that "shadows" the class variable of the same
    s2.school_name = 'XYZ school'
    print(f's2: {s2}')
    print(f's2.school_name: {s2.school_name}')
    # does s1 have a school_name instance variable?
    if s1.school_name is None:
        print('s1 does not have a school_name')
    else:
        if s1.school_name == Student.school_name:
            print(f's1.school_name is identical to Student.school_name: {s1.school_name}')
        else:
            print(f's1.school_name is different from Student.school_name: {s1.school_name}')



