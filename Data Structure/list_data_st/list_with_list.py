student = [
    ["Alice",20,"A"],
    ["Bob",21,"A+"],
    ["Peter",22,"B"]
]
print(student)

print("")
print("--" * 20)
print("Student Details")
print(f"Name: {student[0][0]}, Age: {student[0][1]}, Grade: {student[0][2]}")
print("--" * 20)
print("")

for item in student:
    print(item)
    print(f"Name: {item[0]}, Age: {item[1]}, Grade: {item[2]}")
print("--" * 20)
print("")

student.append(["Iman",21,"A+"])
print(student)
student.insert(2,["Ram",23,"C"])
print(student)
print("--" * 20)
print("")

found:int = int(input("Enter the age: "))
st_found = [item for item in student if item[1] == found]
if student:
    print(st_found[0])
    print(f"Name: {st_found[0][0]}, Age: {st_found[0][1]}, Grade: {st_found[0][2]}")
else:
    print("No student found with that age.")
print("--" * 20)
print("")

student.sort()
print(student)
print("--" * 20)
print("")