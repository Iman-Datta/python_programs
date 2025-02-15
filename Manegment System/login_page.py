def menu():
    print("1 : Create account")
    print("2 : Log in")
    print("3 : Users details")
    print("4 : Exit")
    while True:
        try:
            choice = int(input("Enter your choice (1-4): "))
            if choice in [1, 2, 3, 4]:
                return choice
            else:
                print("Please enter a valid option: 1, 2, 3, or 4")
        except ValueError:
            print("Invalid input. Please enter a number (1-4).")


def create_account(user_dic):
    user_name = input("Enter a unique username: ")
    if user_dic[user_name]:
        print("This username already exists, try again.")
        return # problem
    ft_name = input("Enter your first name: ")
    lt_name = input("Enter your last name: ")
    while True:
        paswd = input("Enter a new password: ")
        repaswd = input("Enter the same password again: ")
        if paswd == repaswd:
            break
        else:
            print("Passwords do not match. Please try again.")

    user_dic[user_name] = {
        "first_name": ft_name,
        "last_name": lt_name,
        "password": paswd,
    }
    
    print(f"Account created successfully for user: {ft_name}!")


def log_in(user_dic):
    user_name = input("Enter your username: ")
    if not user_dic[user_name]:
        print("Username not found. Please try again.")
        return

    paswd = input("Enter your password: ")
    if paswd == user_dic[user_name]["password"]:
        print(f"Login successful. Welcome back, {user_dic[user_name]['first_name']}!")
    else:
        print("Incorrect password. Please try again.")


def users_details(user_dic):
    if not user_dic:
        print("No users registered yet.")
        return

    print("\nRegistered Users:")
    for username, details in user_dic.items(): # Problem
        print(f"Username: {username}, Name: {details['first_name']} {details['last_name']}")


if __name__ == "__main__":
    user_dic = {}
    while True:
        choice = menu()
        if choice == 1:
            create_account(user_dic)
        elif choice == 2:
            log_in(user_dic)
        elif choice == 3:
            users_details(user_dic)
        elif choice == 4:
            print("Exiting program. Goodbye!")
            break