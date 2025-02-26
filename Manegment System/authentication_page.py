class Authentication:
    def __init__(self):
        self.account = []
        self.sl_no = 0

    def menu(self):
        print("-" * 50)
        print("1: Create Account")
        print("2: Login Account")
        print("3: Show Accounts Details")
        print("4: Exit")
        print("-" * 50)

        while True:
            try:
                choice = int(input("Enter your choice (1 to 4): "))
                if choice in [1,2,3,4]:
                    return choice
                else:
                    print("Please enter a valid option: (1 to 4)")
            except ValueError:
                print("Invalid input. Please enter a number (1-4).")

    def create(self):
        print("-" * 50)
        print("------CREATE YOUR ACOOUNT------")
        while True:
            user_nm = input("Enter a unique user name: ")
            if any(user['usnm'] == user_nm for user in self.account): # from AI
                print("This username already exists, try again")
                break
            else:
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
                # We are creating a new dict for storing user info.          
                user: dict = {
                    'usnm' : user_nm,
                    'sl' : self.sl_no,
                    'fnm' : fnm,
                    'lnm' : lnm,
                    'passw' : re_passw,
                }
                # Inserting the dict within a list
                self.account.append(user)
            print(f"Account created successfully for user: {fnm}!")
            break

    def login(self):
        usnm = input("Enter your user name: ")
        user = [item for item in self.account if item['usnm'] == usnm]
        # running a loop over list where each index of the list has a dict.
        if not user:
            print("Username does not exist. Try again.")
            return
        while True:
            try:
                passw = int(input("Enter your password: "))
                if passw == user[0].get('passw'):
                    print(f"Welcome back!")
                    return
                else:
                    print("Incorrect password. Try again.")
            except ValueError:
                print("Your password should be in numbers.")
            
    def show(self):
        if not self.account:  # Access the class variable directly
            print("No student records available.")
            return
        else:
            print("\nUser Information:")
            print("-" * 50)
            for item in self.account:
                print(f"Serial number: {item['sl']}")
                print(f"Name: {item['fnm']} {item['lnm']}")
                print("-" *50)

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
        else:
            break