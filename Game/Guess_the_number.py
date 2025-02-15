import random 
def number_guessing():
    secret_number = random.randint(0,9)

    attempts = 3
    for i in range(1, attempts + 1):
        try:
            guess = int(input("For attempt: {} .Enter your guess: ".format(i)))
        except ValueError:
            print("Enter a valid number")
            continue

        if guess == secret_number:
            print("Congratulations! You guessed the number correctly: ", secret_number)
            break
        elif guess < secret_number:
            print("Too low!")
        else:
            print("Too high!")

        if i < attempts:
            print("Try again.")
        else:
            print("Game over! The correct number was {}.".format(secret_number))

if __name__ == "__main__":
    print("Welcome to the Number Guessing Game!")
    print("You have 3 chances to guess the number (0-9).")
    number_guessing()