class BankAccount:
    def __init__(self, account_number, holder_name, balance=0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance: float = balance
        
    def transfer(self, recipient, amount: float):
        if 0 < amount <= self.balance:
            self.balance -= amount
            recipient.balance += amount
            print(f"₹{amount} transferred from {self.holder_name} to {recipient.holder_name}.")
        else:
            print("Transfer failed due to insufficient funds or invalid amount.")

    def display_balance(self):
        print(f"{self.holder_name}'s Account Balance: ₹{self.balance}")

if __name__ == "__main__":
    account1 = BankAccount("1001", "Iman", 5000)
    account2 = BankAccount("1002", "Ram", 3000)

    while True:
        print("\n1. Iman transfers to Ram")
        print("2. Ram transfers to Iman")
        print("3. Show balances")
        print("4. Exit")

        choice = input("Choose an option: ")
        if choice == "1":
            amount = float(input("Enter amount to transfer from Iman to Ram: "))
            account1.transfer(account2, amount)

        elif choice == "2":
            amount = float(input("Enter amount to transfer from Ram to Iman: "))
            account2.transfer(account1, amount)

        elif choice == "3":
            account1.display_balance()
            account2.display_balance()
        elif choice == "4":
            print("Exiting...")
        else:
            print("Invalid choice. Please choose a valid option.")