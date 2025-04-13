from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Student(Base):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    age = Column(Integer, nullable=False)
    grade = Column(String, nullable=False)

    def __init__(self, name, email, age, grade):
        self.name = name
        self.email = email
        self.age = age
        self.grade = grade