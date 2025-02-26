import random

# Deposit Money, Withdraw Money, Check Balance, Transfer Money (Between Users), Transaction History, Account Details & Security Settings, Close Account

class User:
    def __init__(self):
        self.staff_account = [] # Creating list to store data of employee
        self.user_account = [] # Creating list to store data of user
        self.staff_id = 0 # id for employee
        self.used_acc_numbers = set() # Store the all account numbers of users
        self.balence = 0 # initial balence of users.

    def menu(self):
        print("-" * 50)
        print("1: Create Account")
        print("2: Change account pin")
        print("3: Account Details")

        while True:
            try:
                choice = int(input("Enter your choice (1 to 3): ")) # Taking input from user
                if choice in [1,2,3]:
                    return choice
                else:
                    print("Please enter a valid option: (1 to 3)")
            except ValueError:
                print("Invalid input. Please enter a number (1 to 3).")
    
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
        print("1: Bank Staff Account")
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

        if choice == 1: # For Bank Staff
            while True:
                usnm_staff = input("Enter a unique username: ")
                staff_found = any(item['usnm'] == usnm_staff for item in self.staff_account) # Checking username                
                if not staff_found:
                    fnm = input("Enter your first name: ")
                    lnm = input("Enter your last name: ")
                    while True:
                            passw = input("Enter a new password: ")
                            re_passw = input("Re-enter your password: ")
                            if passw == re_passw:
                                break
                            else:
                                print("Passwords do not match. Please try again.")
                    self.staff_id += 1  # Increment staff ID only after successful creation
                    staff_detail = {  # Creating user dict for staff
                        'id': self.staff_id,
                        'usnm': usnm_staff,
                        'password': passw,
                        'fnm': fnm,
                        'lnm': lnm,
                    }
                    self.staff_account.append(staff_detail)  # Insert into staff list
                    print(f"Welcome {fnm}!")
                    break
                else:
                    print("Username already exists. Please choose a unique username and try again.")
                    break

        else: # For Customer 
            while True:
                while True:
                    try:
                        aadha_no = int(input("Enter your Aadhaar card number: "))
                        if 100000000000 <= aadha_no <= 999999999999:
                            break
                        else:
                            print("Invalid Aadhaar number! Please enter a 12-digit number.")
                    except ValueError:
                        print("Your Aadhaar number should in numbers.")
                existing_user = next((user for user in self.user_account if user['aadhaarno'] == aadha_no), None)
                balence = self.balence
                acc_no = self.generate_acc_no()  # Generate unique account number
                pin = self.generate_pin_no()  # Generate random PIN
                if existing_user: # Aadhaar no exist, Add a new account
                    user = [item for item in self.user_account if item['aadhaarno'] == aadha_no]
                    user_dict = user[0]
                    # print(user_dict)
                    user_dict['accounts'].append({
                        'id': acc_no,
                        'pin': pin,
                        'balence' : balence,
                        })
                else: # New account
                    while True:
                        usnm = input("Enter a unique user name: ")
                        if any(user['usnm'] == usnm for user in self.user_account):
                            print("This username already exists, try again.")
                            continue
                        fnm = input("Enter your first name: ")
                        lnm = input("Enter your last name: ")
                        break

                    user_detail = {
                    'usnm': usnm,
                    'aadhaarno': aadha_no,
                    'fnm': fnm,
                    'lnm': lnm,
                    'accounts': # Initialize accounts list with the first account
                        [
                            {
                            'id': acc_no,
                            'pin': pin,
                            'balence' : balence,
                            }
                        ],
                    }
                    self.user_account.append(user_detail)
                    print(f"Welcome! Your new account has been created successfully.")
                print(f"Account Number: {acc_no}")
                print(f"PIN: {pin} (Keep it safe!)")
                print(self.user_account)
                break

    def change_pin(self):
        try:
            aadh = int(input("Enter your Aadhaar card number: "))
        except ValueError:
            print("Your Aadhaar number should in numbers.")
        # usnm = input("Enter your user name: ")
        user_list = [user for user in self.user_account if user['aadhaarno'] == aadh] # item is the dict and user_list is the list which contain one dict only
        if user_list:
            accno = int(input("Enter your account number: "))
            acc = user_list[0].get('accounts')
            acc_found = acc[0]
            if accno == acc_found['id']: # Account number
                while True:
                    try:
                        new_pin = int(input("Enter your new 4-digit pin: "))
                        if 1000 <= new_pin <= 9999:  # Checking if the PIN is exactly 4 digits
                            re_new_pin = int(input("Re-enter the same 4-digit pin: "))
                            if re_new_pin == new_pin:
                                acc_found['pin'] = re_new_pin
                                print("Your pin has been successfully changed.")
                                break
                            else:
                                print("Pins do not match. Please try again.")
                        else:
                            print("PIN must be exactly 4 digits.")
                    except ValueError:
                        print("Invalid input. PIN must be a 4-digit number.")
            else:
                print("Accont number not found.")
        else:
            print("Invalid input")

    def deposit(self):
        pass

    def withdraw(self):
        pass

    def check_balance(self):
        pass

    def tranasction_hist(self):
        pass

    def acc_details(self): # For bank staff only
        usnm = input("Enter your user name: ")
        staff_found = [staff for staff in self.staff_account if staff['usnm'] == usnm]
        if not staff_found:
            print("nvalid username. Please try again.")
            return
        
        passw = input("Enter your password: ")
        if passw == staff_found[0].get('password'):
            print(f"Login successful. Wllcome back {staff_found[0].get('fnm')}\n")
            print("-" *50)
            try:
                customer_adh_no = int(input("Enter the customer's Aadhar number: "))
                user = [item for item in self.user_account if item['aadhaarno'] == customer_adh_no]
                if user:
                    print(user)
                else:
                    print("User not found.")
            except ValueError:
                print("Account number should be in numbers.")

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
        elif choice == 3:
            us_authentication.acc_details()
        else:
            break