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
    # WARNING: this will create a student instance variable of type Student
    #          that "shadows" the class variable of the same name and type.
    s2.__school = School('XYZ_School', '9876 E. Main', 1700)
    print(f'after  s2: {s2}')
    if hasattr(s2,'__school'):
        print(f'after s2.__school (instance): {s2.__school}')
    else:
        print('s2 does not have an instance variable named __school')

    s2.show()
    
    # Now go back and look at Student s1 to see if its School was affected by
    # what we did to Student s2:
    print(f'after  s1: {s1}')
    if hasattr(s1,'__school'):
        print(f'after s1.__school: {s1.__school}')
    else:
        print('s1 does not have an instance variable named __school')
    s1.show()
