from sqlalchemy import inspect
from model import Base, Student
from db_connection import engine

def create_student_table():
    if engine:
        inspector = inspect(engine)

        if Student.__tablename__ in inspector.get_table_names():
            print("Table Stiudent exist")
        else:
            try:
                Base.metadata.create_all(engine)
                print('Table Student created')
            except Exception as e:
                print(f'Exception in Table {e}')
    else:
        print('No Active database')

if __name__ == "__main__":
    create_student_table()

