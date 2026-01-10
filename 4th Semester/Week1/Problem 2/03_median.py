def findMedian(list, n):
    list.sort()
    if n % 2 == 1:
        return lst[n // 2]
    else:
        return (lst[n // 2 - 1] + lst[n // 2]) / 2
if __name__ == '__main__':
    n = int(input("Enter number of elements: "))
    lst = []

    for i in range(n):
        x = int(input("Enter element: "))
        lst.append(x)
    
    median = findMedian(lst, n)
    print("Median:", median)