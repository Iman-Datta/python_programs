class Student:
    def __init__(self, name: str, roll: int):
        self.name = name
        self.roll = roll
    
    def display_student(self):
        print(f"Name: {self.name}, Roll: {self.roll}")