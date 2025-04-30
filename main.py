from bank import BankAccount
from auth import login
import sys

def show_menu():
    print("\n" + "="*30)
    print("BANK MANAGEMENT SYSTEM")
    print("="*30)
    print("1. Create Account\n2. Deposit\n3. Withdraw\n4. Exit")

def create_account():
    acc_no = input("Enter account number: ")
    name = input("Enter customer name: ")
    return BankAccount(acc_no, name)

if __name__ == "__main__":
    if not login():
        sys.exit("Login failed")
    
    account = None
    while True:
        show_menu()
        choice = input("Enter choice (1-4): ")
        
        if choice == "1":
            account = create_account()
            print("Account created!")
        elif choice == "2" and account:
            amount = float(input("Deposit amount: "))
            print(account.deposit(amount))
        elif choice == "3" and account:
            amount = float(input("Withdraw amount: "))
            print(account.withdraw(amount))
        elif choice == "4":
            sys.exit("Thank you for banking with us")
        else:
            print("Invalid choice or no account created")
