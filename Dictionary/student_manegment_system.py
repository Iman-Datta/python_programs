def menu() -> int:
    print("---------- Student Management System ---------------")
    print("1. Add student: ")
    print("2. Display all students: ")
    print("3. Search student: ")
    print("4. Exit: ")


    while True:
        try:
            choice = int(input("Enter your choice (1-4): "))
            if choice in [1,2,3,4]:
                return choice
            else:
                print("Invalid choice, Enter a valid choice (1-4)")
        except ValueError:
            print("Invalid input, Enter a valid number")

def grade() :
    while True: 
        total_marks = 200
        a_marks = int(input("Marks obtain in subject A (0 to 100): "))
        b_marks = int(input("Marks obtain in subject B (0 to 100): "))
        total_obtain_marks = a_marks + b_marks
        marks_percentage = (total_obtain_marks / total_marks) * 100
        if marks_percentage >= 90 and 90 <= 100:
            return("Grade A+")
        elif marks_percentage >= 80 and 80 <= 89:
            return("Grade A")
        elif marks_percentage >= 70 and 70 <= 79:
            return("Grade B+")
        elif marks_percentage >= 60 and  60 <= 69:
            return("Grade B")
        elif marks_percentage >= 50 and 50 <= 59:
            return("Grade C")
        else:
            print ("Fail")
        break

def add_student(student_dict):
    id = len(student_dict) + 1
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    rank = grade()
    
    # Dic in Python works on the concept of Key-Value pair, where key will be unique
    student_dict[id] = {
        "name": name,
        "age": age,
        "grade": rank,
    }
    # print("Record: {}".format(student_dict))

def display_student(student_dict):
    if not student_dict:
        print("No student found")
    else:
        print("---- List of students ---")
        for details in student_dict.items():
            print("ID: ".format(details[0]), end="")
            print("Name: {} Total: {} percentage: {}".format(details[1]["name"], details[1]["age"], details[1]["grade"]))


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
    student_dict = {}                  
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

if __name__ == "__main__":
    main()