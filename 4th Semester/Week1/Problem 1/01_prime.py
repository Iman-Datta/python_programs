import math

def isPrimeMethodOne(num):
    if num <= 1:
        return False
    for i in range (2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def isPrimeMethodTwo(num):
    if num <= 1:
        return False
    status = True
    for i in range (2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            status = 1
            break
        else:
            status = 0
    return status == 0

def isPrimeMethodThree(num):
    if num <= 1:
        return False
    else:
        count = 0
        for i in range (2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                count += 1
                break
    return count == 0

if __name__ == "__main__":
    num = int(input("Enter a number: "))

# Method 1:
    if isPrimeMethodOne(num):
        print(f"{num} is a prime number using 1st method")
    else:
        print(f"{num} is not a prime number using 1st method")

# Method 2:
    if isPrimeMethodTwo(num):
        print(f"{num} is a prime number using 2nd method")
    else:
        print(f"{num} is not a prime number using 2nd method")

# Method 3:
    if isPrimeMethodThree(num):
        print(f"{num} is a prime number using 3rd method")
    else:
        print(f"{num} is not a prime number using 3rd method")