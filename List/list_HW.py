library=[]
sz: int = 0

#Infinity loop for input
while True:
    car_no = int(input("Enter your car number: "))
    library.append(car_no)
    sz = len(library)
# Sorting
    for i in range(0,sz):
        for j in range(0,sz-1-i):
            if library[j]>library[j+1]:
                temp = library[j]
                library[j]=library[j+1]
                library[j+1]=temp
# After Sorting
    print("The sorted car numbers: ")
    for i in range(0,sz):
        print(library[i], end=" ")