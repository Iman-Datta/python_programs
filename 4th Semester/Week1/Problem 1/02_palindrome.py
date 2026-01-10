def isPalindromeMethodOne(num):
    if num == int(str(num)[::-1]):
        return True
    else:
        return False
    
def isPalindromeMethodTwo(num):
    temp = num
    rev = 0

    while temp > 0:
        dig = temp % 10
        rev = rev * 10 + dig
        temp = temp // 10 # Floor Division Operator

    return num == rev

if __name__ == "__main__":
    num = int(input("Enter a number: "))
    if isPalindromeMethodOne(num):
        print(f"{num} is a palindrome number using 1st method")
    else:
        print(f"{num} is not a palindrome number using 1st method")

    if isPalindromeMethodTwo(num):
        print(f"{num} is a palindrome number using 2nd method")
    else:
        print(f"{num} is not a palindrome number using 2nd method")