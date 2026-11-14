
#python program for insufficient fund using exception handling
class InsufficientFundsError(Exception):
    pass

class ATM:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be greater than zero")
        if amount > self.balance:
            raise InsufficientFundsError(
                f"Balance is Rs.{self.balance}, you requested Rs.{amount}"
            )
        self.balance -= amount
        print(f"Withdrawn Rs.{amount}. Remaining: Rs.{self.balance}")

atm = ATM(5000)

for amount in [2000, -100, 9000]:
    try:
        atm.withdraw(amount)
    except InsufficientFundsError as e:
        print("Transaction failed:", e)
    except ValueError as e:
        print("Invalid amount:", e)
    finally:
        print("Please take your card.\n")