from database import Database

class BankAccount:
    def __init__(self, account_no, customer_name, balance=0):
        self.account_no = account_no
        self.customer_name = customer_name
        self.balance = balance
        self.db = Database()
    
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        self.balance += amount
        self.db.log_transaction(self.account_no, "DEPOSIT", amount)
        return f"₹{amount} deposited. New balance: ₹{self.balance}"
    
    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        self.db.log_transaction(self.account_no, "WITHDRAW", amount)
        return f"₹{amount} withdrawn. Remaining: ₹{self.balance}"
