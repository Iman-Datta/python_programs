class User:
    def __init__(self, first_name, last_name, user_name, password, age):
        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name
        self.password = password
        self.age = age

    def display_account(self):
        print("\nAccount Created Successfully!")
        print(f"Name: {self.first_name}")
        print(f"Age: {self.age}")
        print(f"Username: {self.user_name}")

if __name__ == "__main__":
    while True:
        first_name = input("Enter your first name: ")
        last_name = input("Enter your last name: ")
        age = int(input("Enter your age: "))
        user_name = input("Enter your username: ")
        password = int(input("Enter your password: "))

        user = User(first_name, last_name, user_name,password, age)
        user.display_account()