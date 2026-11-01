# 1. Define the Class
class BankAccount:
    def __init__(self, account_holder, initial_balance=0.0):
        self.holder = account_holder      # Instance attribute
        self.balance = initial_balance    # Instance attribute

    # Method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited ₹{amount}. New balance: ₹{self.balance}"
        return "Invalid deposit amount."

    # Method to withdraw money
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return f"Withdrew ₹{amount}. Remaining balance: ₹{self.balance}"
        elif amount > self.balance:
            return "Insufficient funds!"
        return "Invalid withdrawal amount."

    # Method to check balance
    def get_balance(self):
        return f"Account holder: {self.holder} | Current Balance: ₹{self.balance}"


# 2. Create Objects (Independent Accounts)
alex_account = BankAccount("Alex Kumar", 5000.0)
sara_account = BankAccount("Sara Sharma") # Starts with default 0.0


# 3. Perform Operations
print(alex_account.deposit(1500))    # Output: Deposited ₹1500. New balance: ₹6500.0
print(alex_account.withdraw(2000))   # Output: Withdrew ₹2000. Remaining balance: ₹4500.0

print(sara_account.deposit(3000))    # Output: Deposited ₹3000. New balance: ₹3000.0
print(sara_account.withdraw(4000))   # Output: Insufficient funds!

# Final Status Check
print(alex_account.get_balance())    # Output: Account holder: Alex Kumar | Current Balance: ₹4500.0
print(sara_account.get_balance())    # Output: Account holder: Sara Sharma | Current Balance: ₹3000.0
