#for loop


# Write all the letters 
name = 'Iman Datta' 
for i in name:
    print(i)
    if (i == "D"):
        print('something special')


# Write all the elements of lists
colors = ["Red", "Green", "Blue", "Yellow"] 
for color in colors: 
    print(color)
    for i in color:
        print(i)

for i in range(5):
    print(i+1)
print()
for k in range(6,13):
    print(k+1)

for i in range (1,20,3):
    print(i+1)

for i in range(7):  
    for j in range (0,7):
        print(j, end = " ")
    print()
# while loop

i = 0
while(i<=3):
    print(i)
    i = i + 1
i = 0
while (i<=38):
    i = int(input("Enter the number: "))
    print(i)
print("Done with the loop")

i = 5
while(i>0):
    print(i)
    i = i-1
else:
    print("I am inside else")

numbers = [10,20,30,5,15]
max_value = 0
for num in numbers:
    if num>max_value:
        max_value=num

print("the maximum value is: ", max_value)

unsort_list=[14,5,2,6,21,15,12]
sz = len(unsort_list)
for i in range(0,sz):
    for j in range(0,sz-i-1):
        if unsort_list[j]>unsort_list[j+1]:   #swapping or interchenging
            temp=unsort_list[j]
            unsort_list[j] = unsort_list[j+1]
            unsort_list[j+1] = temp

for i in range(0,sz):
    print(i, end = " ")

# grade
while True: 
        total_marks = 200
        a_marks = int(input("Marks obtain in subject A (0 to 100): "))
        b_marks = int(input("Marks obtain in subject B (0 to 100): "))
        total_obtain_marks = a_marks + b_marks
        marks_percentage = (total_obtain_marks / total_marks) * 100
        if marks_percentage >= 90 and 90 <= 100:
            print("Grade A+")
        elif marks_percentage >= 80 and 80 <= 89:
            print("Grade A")
        elif marks_percentage >= 70 and 70 <= 79:
            print("Grade B+")
        elif marks_percentage >= 60 and  60 <= 69:
            print("Grade B")
        elif marks_percentage >= 50 and 50 <= 59:
            print("Grade C")
        else:
            print ("Fail")
        break


a = [50, 89, 43, 78, 10, 32, 98, 41, 33]

max_element_loop = numbers[0]
for number in numbers:
    if number > max_element_loop:
        max_element_loop = number

print("The maximum element in the list using a loop is:", max_element_loop)