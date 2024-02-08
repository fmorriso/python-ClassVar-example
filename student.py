from typing import ClassVar
from school import School


class Student:
    # Class variable (e.g., equivalent to static variable in Java and C#)
    __school: ClassVar[str] = School('ABC School', '123 Main Street', 1600)

    # constructor
    def __init__(self, name: str, roll_no: int):
        self.name = name
        self.roll_no = roll_no

    # Instance method
    def show(self):
        # check for shadow variable the same names as the class variable
        if self.__school is None:
            print(self.name, self.roll_no, Student.__school)
        else:
            print(self.name, self.roll_no, self.__school)

    def __repr__(self):
        # check for shadow variable the same names as the class variable
        if hasattr(self, '__school'):
            return f'name: {self.name}, roll_no: {self.roll_no}, __school (instance): {self.__school}'
        else:
            return f'name: {self.name}, roll_no: {self.roll_no}, __school (ClassVar): {Student.__school}'

