from typing import ClassVar
from school import School


class Student:
    # Class variable (e.g., equivalent to static variable in Java and C#)
    school: ClassVar[School] = School('ABC School', '123 Main Street', 1600)

    # constructor
    def __init__(self, name: str, roll_no: int):
        self.name = name
        self.roll_no = roll_no

    def __str__(self):
        return f'name: {self.name}, roll_no: {self.roll_no}, school: {self.school}'

