class Authentication():
    def __init__(self):
        Authentication.account = []
        Authentication.sl_no = 1
    def menu(self):
        print("-" * 50)
        print("1: Create Account")
        print("2: Login Account")
        print("3: Show Accounts Details")
        print("4: Search Account")
        print("5: Exit")
        print("-" * 50)
        while True:
            try:
                choice = int(input("Enter your choice (1 to 5): "))
                if choice in [1,2,3,4,5]:
                    return choice
                else:
                    print("Please enter a valid option: (1 to 5)")
            except ValueError:
                print("Invalid input. Please enter a number (1-5).")

    def create(self):
        print("-" * 50)
        print("------CREATE YOUR ACOOUNT------")
        while True:
            user_nm = input("Enter a unique user name: ")
            if user_nm in self.account:
                print("This username already exists, try again")
            else:
                pass
            fnm = input("Enter your first name: ")
            lnm = input("Enter your last name: ")
            self.sl_no += 1
            while True:
                try:
                    passw = int(input("Enter your new password (in numbers): "))
                    re_passw = int(input("Enter same password: "))
                    if re_passw == passw:
                        break
                    else:
                        print("Passwords do not match. Please try again.")
                except ValueError:
                    print("Your password should in numbers.")
                
                
            
            user: dict = {
                'sl' : self.sl_no,
                'fnm' : fnm,
                'lnm' : lnm,
                'passw' : re_passw,
            }

            print(f"Account created successfully for user: {fnm}!")
            break

    def login(self):
        while True:
            usnm = input("Enter your user name: ")
            if usnm in self.account:
                pass
            else:
                print("Does not exit")
            passw = int(input("Enter your password: "))

    # def show(self):
    #     if not Authentication.account:
    #         print("No student records available.")
    #         return
    #     else:
    #         print(self.account)
    def show(self):
        if not Authentication.account:  # Access the class variable directly
            print("No student records available.")
            return
        else:
            print(Authentication.account)  # Access the class variable directly




if __name__ == "__main__":
    acc = Authentication()
    while True:
        choice = acc.menu()
        if choice == 1:
            acc.create()
        elif choice == 2:
            acc.login()
        elif choice == 3:
            acc.show()
        elif choice == 4:
            pass
        else:
            break













# def log_in(user_dic):
#     user_name = input("Enter your username: ")
#     if not user_dic[user_name]:
#         print("Username not found. Please try again.")
#         return

#     paswd = input("Enter your password: ")
#     if paswd == user_dic[user_name]["password"]:
#         print(f"Login successful. Welcome back, {user_dic[user_name]['first_name']}!")
#     else:
#         print("Incorrect password. Please try again.")


# def users_details(user_dic):
#     if not user_dic:
#         print("No users registered yet.")
#         return

#     print("\nRegistered Users:")
#     for username, details in user_dic.items(): # Problem
#         print(f"Username: {username}, Name: {details['first_name']} {details['last_name']}")


# if __name__ == "__main__":
#     user_dic = {}
#     while True:
#         choice = menu()
#         if choice == 1:
#             create_account(user_dic)
#         elif choice == 2:
#             log_in(user_dic)
#         elif choice == 3:
#             users_details(user_dic)
#         elif choice == 4:
#             print("Exiting program. Goodbye!")
#             break