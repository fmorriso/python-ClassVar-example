from typing import ClassVar


class School:
    def __init__(self, name: str, address: str, capacity: int):
        self.name = name
        self.address = address
        self.capacity = capacity

    def __repr__(self):
        return f'Name: {self.name}, Address: {self.address}, Capacity: {self.capacity}'
