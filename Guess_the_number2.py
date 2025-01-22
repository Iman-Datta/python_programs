# import random

# def guess_the_number():
#     secret_number = str(random.randint(10000, 99999))  
#     attempts = 3

#     for i in range(1, attempts + 1):
#         while True:
#             try:
#                 guess_number = input("For attempt {}. Enter your guess: ".format(i))
#                 if len(guess_number) == 5 and guess_number.isdigit():
#                     break # PROBLEM
#                 else:
#                     print("Invalid input. Please enter a valid 5-digit number.")
#             except ValueError:
#                 print("Enter a valid number * * * * * * * * * *") # PROBLEM
                
#         if guess_number == secret_number:
#             print("Congratulations! You guessed the number correctly: ", secret_number)
#             return # PROBLEM
#         else:
#             matched_digits = ''.join([guess_number[j] if guess_number[j] == secret_number[j] else '*' for j in range(5)])
#             print("Matching digits in correct positions: ", matched_digits)

#         if guess_number < secret_number:
#             print("Too low!")
#         else:
#             print("Too high!")
            
#         if i < attempts:
#             print("Try again.")
#         else:
#             print("Game over! The correct number was {}.".format(secret_number))

# if __name__ == "__main__":
#     print("Guess The 5 Digit Number")
#     print("You have only three chances.")
#     guess_the_number()


import random

def guess_the_number():
    secret_number = str(random.randint(10000, 99999))  # secret number as a string for easier comparison
    attempts = 3

    for i in range(1, attempts + 1):
        while True:
            guess_number = input(f"For attempt {i}. Enter your guess: ")
            if len(guess_number) == 5 and guess_number.isdigit():
                break 
            elif len(guess_number)!=5:
                print("Invalid input. Please enter a valid 5-digit number.")
            elif guess_number.isdigit()==False:
                print("Enter a valid number")
        
        if guess_number == secret_number:
            print(f"Congratulations! You guessed the number correctly, and it is {secret_number}")
            return
        else:
            matched_digits = ''.join([guess_number[j] if guess_number[j] == secret_number[j] else '*' for j in range(5)])
            print(f"Matching digits in correct positions: {matched_digits}")
        if i!=3:        
            if guess_number < secret_number:
                print("Guess something higher.")
            else:
                print("Guess something lower.")
        
        if i < attempts:
            print("Try again.")
        else:
            print(f"Game over! The correct number was {secret_number}")

if __name__ == "__main__":
    print("Guess The 5 Digi Number")
    print("You have only three chances.")
    guess_the_number()