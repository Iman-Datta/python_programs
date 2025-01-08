# How to print Maximum element from a list
max = list[0]
for element in list:
    if (element > max):
        max = element
print("Max",max)



# How to short a list
unsort_list = [14, 5, 2, 6, 21, 15, 12]
print(type(unsort_list))
size = len(unsort_list)

# before Sorting
print("Unsorted Array")
for i in range(0, size):
    print(unsort_list[i], end=" ")  

print()
# Sorting
for i in range(0, size):
    for j in range(0, size-1-i):
        if unsort_list[j] > unsort_list[j+1]:
            #Swapping or Interchanging
            temp = unsort_list[j]
            unsort_list[j] = unsort_list[j+1]
            unsort_list[j+1] = temp

# After Sorting
print("Sorted Array")
for i in range(0, size):
    print(unsort_list[i], end=" ")