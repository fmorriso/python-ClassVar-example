from typing import ClassVar
class Student:
    # Class variable
    school_name : ClassVar[str]  = 'ABC School '

    # constructor
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    # Instance method
    def show(self):
        print(self.name, self.roll_no, Student.school_name)