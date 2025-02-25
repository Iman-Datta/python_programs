import random

# Deposit Money, Withdraw Money, Check Balance, Transfer Money (Between Users), Transaction History, Account Details & Security Settings, Close Account

class User:
    def __init__(self):
        self.empl_account = [] # Creating list to store data of employee
        self.user_account = [] # Creating list to store data of user
        self.empl_id = 0 # id for employee
        self.used_acc_numbers = set() # Store the all account numbers of users
        self.balence = 0 # initial balence of users.

    def menu(self):
        print("-" * 50)
        print("1: Create Account")
        print("2: Change account pin")

        while True:
            try:
                choice = int(input("Enter your choice (1 to 2): ")) # Taking input from user
                if choice in [1,2]:
                    return choice
                else:
                    print("Please enter a valid option: (1 to 2)")
            except ValueError:
                print("Invalid input. Please enter a number (1-2).")
    
    def generate_acc_no(self):
        while True:
            acc_no = random.randint(1000000, 9999999) # Generate 7-digit number
            if acc_no not in self.used_acc_numbers: # Uniqueness acc number
                self.used_acc_numbers.add(acc_no) # Insert to the set
                return acc_no

    def generate_pin_no(self):
        return random.randint(1000, 9999)
    
    def create(self):
        print("----------CREATE A NEW BANK ACOOUNT----------")
        print("1: Employee Account")
        print("2: User Account")

        while True:
            try:
                choice = int(input("Enter your choice: "))
                if choice in [1,2]:
                    break
                else:
                    print("Please enter a valid option: (1 or 2)")
            except ValueError:
                print("Invalid input. Alease enter a number(1 or 2)")

        if choice == 1: # For employee
            while True:
                usnm = input("Enter a unique user name: ")
                if any(user['usnm'] == usnm for user in self.empl_account): # Running a loop over list where each index of the list has a dict. And 'Any' is a function
                    print("This username already exists, try again")
                    break
                else:
                    fnm = input("Enter your first name: ")
                    lnm = input("Enter your last name: ")
                    self.empl_id += 1
                    while True:
                        try:
                            passw = int(input("Enter a new password: "))
                            re_passw = int(input("Enter the same password: "))
                            if re_passw == passw:
                                break
                            else:
                                print("Passwords do not match. Please try again.")
                        except ValueError:
                            print("Your password should in numbers.")
                        
                    empl_detail: dict = { # Creating user dict for employee
                        'usnm' : usnm,
                        'id' : self.empl_id,
                        'fnm' : fnm,
                        'lnm' : lnm,
                        'passw' : passw,
                    }
                    self.empl_account.append(empl_detail) # Inserting the dict within a list of employee
                    print(f"Wellcome {fnm}")
                    break
        else: # For user
            while True:
                usnm = input("Enter a unique user name: ")
                if any(user['usnm'] == usnm for user in self.user_account): # Same as line no 40
                    print("This username already exists, try again")
                    continue

                fnm = input("Enter your first name: ")
                lnm = input("Enter your last name: ")
                acc_no = self.generate_acc_no()  # Get a unique account number
                pin = self.generate_pin_no()        # Get a random PIN
                user_detail: dict = { # Creating user dict for users
                    'usnm' : usnm,
                    'id' : acc_no,
                    'pin' : pin,
                    'fnm' : fnm,
                    'lnm' : lnm,
                }
                self.user_account.append(user_detail) # Inserting the dict within a list of employee
                print(f"Welcome, {fnm}! Your account has been created successfully.")
                print(f"🔹 Account Number: {acc_no}")
                print(f"🔹 PIN: {pin} (Keep it safe!)")
                break

    def change_pin(self):
        usnm = input("Enter your user name: ")
        usnm_found = [item for item in self.user_account if item['usnm'] == usnm]
        if not usnm_found:
            print("User not found.")
            return
        
        user_data = usnm_found[0]  # Extract the dictionary from the list

        try:
            accno = int(input("Enter your account number"))
            if accno == user_data['id']:
                while True:
                    try:
                        new_pin = int(input("Enter your new 4-digit pin: "))
                        re_new_pin = int(input("Re-enter the same 4-digit pin: "))
                        if 1000 <= new_pin <= 9999:  # Checking if the PIN is exactly 4 digits
                            if re_new_pin == new_pin:
                                user_data['pin'] = re_new_pin
                                print("Your pin has been successfully changed.")
                                break
                            else:
                                print("Pins do not match. Please try again.")
                        else:
                            print("PIN must be exactly 4 digits.")
                    except ValueError:
                        print("Invalid input. PIN must be a 4-digit number.")
            else:
                print("Account number doesnot matched.")
        except ValueError:
            print("Invalid account number. Please enter a number.")

    def deposit(self):
        pass

    def withdraw(self):
        pass

    def check_balance(self):
        pass

    def tranasction_hist(self):
        pass

    def acc_details(self):
        pass

    def close_account(self):
        pass

if __name__ == "__main__":
    us_authentication = User() # Creating obeject of the class User

    while True:
        choice = us_authentication.menu()
        if choice == 1:
            us_authentication.create()
        elif choice == 2:
            us_authentication.change_pin()
        else:
            break