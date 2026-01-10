def findMean(list, n):
    total = 0
    for i in range (n):
        total = total + list[i]
    mean = total / n
    return mean

if __name__ == '__main__':
    n = int(input("Enter number of elements: "))
    lst = []

    for i in range(n):
        x = int(input("Enter element: "))
        lst.append(x)
    
    mean = findMean(lst, n)
    print("Mean:", mean)