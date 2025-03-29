class User:
    def __init__(self):
        self.first_name = ""
        self.last_name = ""
        self.user_name = ""
        self.password = ""
        self.age = 0

    def user_input(self):
        self.first_name = input("Enter your first name: ")
        self.last_name = input("Enter your last name: ")
        self.age = int(input("Enter your age: "))
        self.user_name = input("Enter your username: ")
        self.password = input("Enter your password: ")  # Store as a string

    def display_account(self):
        print("\nAccount Created Successfully!")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Username: {self.user_name}")

# if __name__ == "__main__":
#     while True:
#         user = User()  # Create an empty user object
#         user.user_input()  # Take input
#         user.display_account()  # Display user details
        
#         # Ask if user wants to create another account
#         another = input("Do you want to create another account? (yes/no): ").strip().lower()
#         if another != "yes":
#             break  # Exit the loop