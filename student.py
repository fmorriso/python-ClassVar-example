from typing import ClassVar


class Student:
    # Class variable
    school_name: ClassVar[str] = 'ABC School '

    # constructor
    def __init__(self, name: str, roll_no: int):
        self.name = name
        self.roll_no = roll_no

    # Instance method
    def show(self):
        print(self.name, self.roll_no, Student.school_name)

    def __repr__(self):
        return f'name: {self.name}, roll_no: {self.roll_no}, school: {Student.school_name}'
