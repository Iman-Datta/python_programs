from model import Student
from db_connection import session

def add_student(name, email, age, grade):
    try:
        # Create an object of the model class
        new_student = Student(name=name, email=email, age=age, grade=grade)
        session.add(new_student)    
        session.commit()
        print(f"Student {name} added successfully")
    except Exception as e:
        print(f"Exception occur {e}")
    finally:
        session.close()


if __name__ == "__main__":
    print("Enter student details:")
    name: str = input("Enter name: ")
    email: str = input("Enter email: ")
    age: int = int(input("Enter age: "))
    grade: str = input("Enter grade: ")

    add_student(name, email, age, grade)

