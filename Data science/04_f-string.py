str = "iman"
# string is immutable. So we can not write str[0] = "g"

name = "iman"
age = 21
print("I am {} and I am {} years old".format(name,age)) # Old method
print(f"I am {name} and I am {age} years old") # New method

pi = 3.14159
print(f"Pi rounded to 2 decimal places: {pi:.2f}")

# Alignment
print(f"{'Python':<10}") # Left-align
print(f"{'Python':>10}") # Right-align
print(f"{'Python':^10}") # Center-align