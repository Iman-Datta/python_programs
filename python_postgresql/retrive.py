from model import Student
from db_connection import session

def fetch_students():
    try:
        students = session.query(Student).all()
        if students:
                print('Record of Student table: ')
                for student in students:
                    print(f"ID: {student.id}, Name: {student.name}, Email: {student.email}, Age: {student.age}, Grade: {student.grade}")
                    print("---------------------------------------")
        else:
            print("No data found")
    except Exception as e:
        print(f"Exception occur {e}")
    finally:
         session.close()


if __name__ == "__main__":
     fetch_students()