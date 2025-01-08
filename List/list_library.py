print("List programing")
library = [] # we declare a list by the name called library
total = 0 # variable that will hold summation

library.append(56) # we are initialization the list library
library.append(42)
library.append(77)
library.append(34)
library.append(64)

# checking the size of the list
sz = len(library)
print('Size of the list library is: {}'.format(sz))

# print an element from the list
print('First element of the list library: {}'.format(library[0]))
print('Last element of the list library: {}'.format(library[sz - 1]))

# print all the elements of the list library
# using loop
for cn in range(0,sz):
    print('At index position {} value is {}'.format(cn,library[cn]))

print()

cn = 0
while cn < sz:
    total+=library[cn]
    cn+=1

print('Total is: {}'.format(total))


# Finding maximum & minimum value from the list
max = library[0]
min = library[0]
element = library[0]
for num in library:
    if num > max:
        max = num
print("The maximum value of the element is: {}".format(max))
for num in library:
    if num < min:
        min=num
print("The minimum value of the element is: {}".format(min))


# Short the list
for i in range(sz):
    for j in range(0,sz-1-i):
        if library[j] > library[j+1]:
            temp = library[j]
            library[j] = library[j+1]
            library[j+1] = temp
print("The shorted list: ")

for i in range(0,sz):
    print(library[i], end = " ")