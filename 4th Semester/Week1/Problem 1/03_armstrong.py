def isArmstrong(num):
    temp = num
    sz = len(str(num))
    total = 0

    while temp > 0:
        dig = temp % 10
        total = total + pow(dig, sz)
        temp //= 10


    return num == total

if __name__ == "__main__":
    num = int(input("Enter a number: "))
    if isArmstrong(num):
        print(f"{num} is an Armstrong number")
    else:
        print(f"{num} is not an Armstrong number")