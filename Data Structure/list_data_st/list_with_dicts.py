# List containing Dict
students = [
    {'name': 'Alice', 'age': 20, 'grade':'A'},
    {'name': 'Bob', 'age': 21, 'grade':'A+'},
    {'name': 'Peter', 'age': 22, 'grade':'B'},
]

# Python Memory Management: Automatic Memory Managment with Garbage Collector
# C language Dynamic Memory Allocation
# id() prints the address of an identifier object
# print('Address of students: {}'.format(id(students)))           # this object resides inside Stack memory
# print('Address of first dictionary: {}'.format(id(students[0])))  
# print('Address of second dictionary: {}'.format(id(students[1])))  

for row in students:
    print(row)

print(f"Name: {students[1]['name']}, Age: {students[1]['age']}")

students[1]['grade'] = 'B+'

# for row in students:
#     print(row)

students.append({'name': 'Susan', 'age': 21, 'grade':'A'})

# for row in students:
#     print(row)

# Sorting of the list using age field
# Lambda Function: Is meanto make the function smal  & precise
students.sort(key= lambda x:  x['age'], reverse=True)

print("\n")

# keys()
# values()
# items()
# for row in students:
#     for k,v in row.items():
#         print(f'{k}: {v}',end=" ")
#     print("")

for row in students:
    for k,v in row.items():
        print(f'{v}',end=" ")
    print("")




















