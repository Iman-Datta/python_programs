import sys

# Package & Module
# class, object, constructor, method

class Stack:
    def __init__(self):
        self.stack = []
        self.roll = 1
    
    # Method responsible for inserting a new instance
    def push(self, fname: str, lname: str, physics: float, chem: float ):
        student: dict = {                             # Created a Dict
            'roll': self.roll,
            'fname': fname,
            'lname': lname,
            'physics': physics,
            'chem': chem
        }
        self.stack.append(student)
        print("New record inserted")
        self.roll += 1

    def display(self):
        print("Student info: ")
        for item in self.stack:
            print(f'Row: {item}')                       # It will run for each row, so it will show the 1st dict, then 2nd dict and so on
            for key, value in item.items():
                if key == 'fname' or key == 'lname':
                    print(key, value)
            
            #print(f'First name: {single['fname']} last name: {single['lname']}')                        
            # [0][3]            # Slicing
            # [1][3]

    def insert(self,fname: str, lname: str, physics: float, chem: float):
        student: dict = {                             # Created a Dict
            'roll': self.roll,
            'fname': fname,
            'lname': lname,
            'physics': physics,
            'chem': chem
        }
        self.stack.append(student)
        sz = len(self.stack)
        print(sz)



if __name__ == "__main__":
    ref: Stack = Stack()
    while True:
        print("\n-----------Choice----------")
        print("1. Insert new student:")
        print("2. Display students: ")
        print("3: Insert a student in between: ")
        print("5: Exit")
        choice = int(input("Enter the choice: "))
        if choice == 1:
            fname = input("Enter first name: ")
            lname = input("Enter last name: ")
            physics = float(input("Enter mark of Physics: "))
            chem = float(input("Enter mark of Chemistry: "))
            # When we call a method, that is present inside the class, we need to make use of '.' Period operator
            # so, instance followed by Period and the name of the method
            ref.push(fname, lname, physics, chem)
        if choice == 2:
            ref.display()
        if choice == 3:
            ref.insert()
        if choice == 5:
            sys.exit()
