def is_four_digit_number(n):
    return 1000 <= n <= 9999  # Ensures it's a 4-digit integer

try:
    user_input = int(input("Enter a 4-digit number: "))
    if is_four_digit_number(user_input):
        print("Valid 4-digit number")
    else:
        print("Invalid input")
except ValueError:
    print("Invalid input. Please enter a number.")