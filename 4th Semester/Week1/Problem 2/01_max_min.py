def find_max_min(list, n):
    max = list[0]
    min = list[0]
    for i in range (n):
        if list[i] > max:
            max = list[i]
        if list[i] < min:
            min = list[i]
    return max, min

if __name__ == '__main__':
    n = int(input("Enter number of elements: "))
    lst = []

    for i in range(n):
        x = int(input("Enter element: "))
        lst.append(x)

    mx, mn = find_max_min(lst, n)
    
    print("Maximum:", mx)
    print("Minimum:", mn)