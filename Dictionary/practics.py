def menu() -> int:
    print("---------- Student Management System ---------------")
    print("1. Add student: ")
    print("2. Display all students: ")
    print("3. Search student: ")
    print("4. Exit: ")

    while True:
        # Exception Handling (So, based on wrong input format, the app will show the message, otherwise it would continue)
        try:
            choice = int(input("Enter your choice (1-4): "))
            if choice in [1,2,3,4]:
                return choice
            else:
                print("Invalid choice, Enter a valid choice (1-4)")
        except ValueError:
            print("Invalid input, Enter a valid number")

def add_student(student_dict):
    id = len(student_dict) + 1
    while True:
        name = input("Enter student name: ")
        if all(part.isalpha() for part in name.split()):           # part: ['Swarup','Kumar','Saha']
            break
        else:
            print("Invalid input, give letters")

    while True: 
        try:     
            java = int(input("Enter mark for Java: "))
            if 0< java <101:
                break
            else:
                print("Out of the range")
        except ValueError:
            print("Invalid input, give digits")

    while True: 
        try:     
            python = int(input("Enter mark for Python: "))
            if 0< python <101:
                break
            else:
                print("Out of the range")
        except ValueError:
            print("Invalid input, give digits")

    fm = 200
    total = java + python
    percentage = (total/fm)*100
    
    # Dic in Python works on the concept of Key-Value pair, where key will be unique
    student_dict[id] = {
        "name": name,
        "java": java,
        "python": python,
        "total": total,
        "percentage": percentage,

    }
    print(type(student_dict))
    print("Record saved successfully")

def display_student(student_dict):
    if not student_dict:
        print("No student found")
    else:
        print("---- List of students ---")
        for details in student_dict.items():
            # print(details)
            print("ID: {} ".format(details[0]),end="")
            # print("Details: {}".format(details[1]))
            print("Name: {} Total: {} percentage: {}".format(details[1]["name"], details[1]["total"], details[1]["percentage"]))

def search_student(student_dict):
    status: int = 0
    search_name = input("Enter the name of the student: ")
    for details in student_dict.items():
        if search_name in details[1]["name"]:
            print("Student found. Here is the details: {}".format(details))
            status = 1
            break
    
    if(status == 0):
        print("Student not found")

def main():
    student_dict = {}                   # Dictionary is a Data structure in python
    while True:
        choice = menu()
        if choice == 1:
            add_student(student_dict)
        elif choice == 2:
            display_student(student_dict)
            pass
        elif choice == 3:
            search_student(student_dict)
            pass
        elif choice == 4:
            print("Exiting from the program")
            break
        else:
            print("Invalid choice")

def input_fn(name):
    return name[::-1]

if __name__ == "__main__":
    # main()
    username = input("Enter your name:" )
    reverse = input_fn(username)
    print(reverse)
