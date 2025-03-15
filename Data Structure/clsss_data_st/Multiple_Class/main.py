from studentMark import StudentMark

def main():
    student = StudentMark()
    
    while True:
        name = input('Enter name: ')
        roll = int(input('Enter roll: '))
        phy = int(input('Enter phy: '))
        chem = int(input('Enter chem: '))
        maths = int(input('Enter maths: '))

        student.add_student(name, roll, phy, chem, maths)

        student.display_all()


if __name__ == "__main__":
    main()
