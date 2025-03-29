from user import User

def main() :
    while True:
        user = User()  # Create an empty user object
        user.user_input()  # Take input
        user.display_account()  # Display user details
        
        # Ask if user wants to create another account
        another = input("Do you want to create another account? (yes/no): ").strip().lower()
        if another != "yes":
            break  # Exit the loop

if __name__ == "__main__":
    main()