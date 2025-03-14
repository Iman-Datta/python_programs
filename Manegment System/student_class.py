class Student:
    def __init__(self):
        Student.stack = []
        Student.roll = 1

    def menu(self):
        while True:
            print("\n-----------Choice----------")
            print("1. Insert new student:")
            print("2: Insert a student in between: ")
            print("3: Display students: ")
            print("4: Search student via name: ")
            print("5: Exit")
            try:
                choice = int(input("Enter the choice: "))
                if choice in [1,2,3,4,5]:
                    return choice
                else:
                    print("Enter a valid choice (1-5).")
            except ValueError:
                print("Invalid input.Please enter a number.")

    def push(self):
        fname = input("Enter your first name: ")
        lname = input("Enter your last name: ")
        while True:
            try:
                ag = int(input("Enter your age: "))
                break
            except ValueError:
                print("Please enter a valid number for age.")
        while True:
            try:
                physics = int(input("Enter mark of Physics: "))
                break
            except ValueError:
                print("Please enter a valid number for age.")
        while True:
            try:
                chem = int(input("Enter mark of Chemistry: "))
                break
            except ValueError:
                print("Please enter a valid number for age.")

        student: dict = {                             
            'roll': self.roll,
            'fname': fname,
            'age' : ag,
            'lname': lname,
            'physics': physics,
            'chem': chem
        }
        self.stack.append(student)
        print("New record inserted")
        self.roll += 1

    def insert(self):
        fnm = input("Enter your first name: ")
        lnm = input("Enter your last name: ")
        while True:
            try:
                physics = int(input("Enter mark of Physics: "))
                break
            except ValueError:
                print("Please enter a valid number for age.")
        while True:
            try:
                chem = int(input("Enter mark of Chemistry: "))
                break
            except ValueError:
                print("Please enter a valid number for age.")
        while True:
            try:
                ag = int(input("Enter your age: "))
                break
            except ValueError:
                print("Please enter a valid number for age.")
        
        student: dict = {
            'roll' : self.roll,
            'fname' : fnm,
            'lname' : lnm,
            'age' : ag,
            'phy' : physics,
            'chem' : chem,
        }
        while True:
            try:
                index = int(input("Enter your index: "))
                if 0 <= index <= len(Student.stack):
                    break
                else:
                    print(f"Please enter a valid index between 0 and {len(Student.stack)}.")
            except ValueError:
                print("Invalid Input")
        Student.stack.insert(index,student)

        print("New record inserted")
        Student.roll += 1

    def display(self):
        if not self.stack:
            print("No student records available.")
            return

        print("\nStudent Information:")
        print("-" * 50)
        for student in self.stack: # student is Dict here
            # Handle inconsistency in physics key naming between push and insert methods.
            physics_marks = student.get('physics', student.get('phy', 'N/A'))
            print(f"Roll Number : {student['roll']}")
            print(f"Name        : {student['fname']} {student['lname']}")
            print(f"Age         : {student['age']}")
            print(f"Physics     : {physics_marks}")
            print(f"Chemistry   : {student['chem']}")
            print("-" * 50)

    def search(self):
        fname = input("Enter first name: ")
        found = [item for item in self.stack if item['fname'] == fname]
        if found:
            print("\nSearch Results:")
            print("-" *50)
            for item in found:
                print(f"Roll No: {item['roll']}")
                print(f"Name: {item['fname']} {item['lname']}")
                print(f"Age: {item['age']}")
                print(f"Physics Marks: {item['physics']}")
                print(f"Chemistry Marks: {item['chem']}")
                print("-" *50)
        else:
            print("No student found with that name.")

if __name__ == '__main__':
    ob_student = Student()
    while True:
        choice = ob_student.menu()
        if choice == 1:
            ob_student.push()
        elif choice == 2:
            ob_student.insert()
        elif choice == 3:
            ob_student.display()
        elif choice == 4:
            ob_student.search()
        else:
            print("Program Ending")
            break