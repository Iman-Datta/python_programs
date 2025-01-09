def menu():
    print("1 : create account")
    print("2 : Log in")
    print("3 : Users details")
    print("4 : Exist")
    while True:
        try:
            choice = int(input("Enter your choice (1-3): "))
            if choice in [1,2,3,4]:
                return choice
            else:
                print("Please enter a valid option: 1, 2,3 or 4")
        except ValueError:
            print("Invalid input. Please enter a number (1-3)")


def create_account():
    user_name = input("Enter a unique username: ")
    if user_name in user_dic:
        print("This username is already exists, try again.")
    else:
        return user_name
    ft_name = input("Enter your first name: ")
    lt_name = input("Enter your last name: ")
    while True:
        paswd = input("Enter a new password: ")
        repaswd = input("Enter the same password again: ")
        if paswd == repaswd:
            break
        else:
            print("Passwords do not match. Please try again.")

    user_dic = {
        "username" : user_name,
        "fast_name" : ft_name,
        "last_name" : lt_name,
        "password" : paswd,
    }

    print("Account created successfully for user:{} ".format(user_dic["fast_name"]))
    
def log_in():
    # while True:
        user_name = input("Enter your user name: ")
        if user_name not in user_dic["username"]:
            print("User name not found. Please try again.")

            # Problem
            
        paswd = input("Enter your password: ")
        if paswd == user_dic["password"]:
            print("login successfully.Welcome back {}".format(user_dic["username"]))
        else:
            print("Incorrect password. Please try again")



# def Users_details() :

if __name__ == "__main__":
    user_dic = {}
    while True:
        choice = menu()
        if choice == 1:
            create_account()
        elif choice == 2:
            log_in()
        else:
            break
