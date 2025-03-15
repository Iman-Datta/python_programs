from student import Student
from mark import Mark

class StudentMark:
    def __init__(self):
        self.students: list = []

    def add_student(self, name: str, roll: int, physics: int, chemistry: int, maths: int):
        # we created an instance of the student & mark classes
        student = Student(name, roll)
        mark = Mark(physics, chemistry, maths)
        self.students.append((student, mark))           # List that hold in every index a Tuple
    
    def display_all(self):
        for student, mark in self.students:
            print(student," ",mark)



    

