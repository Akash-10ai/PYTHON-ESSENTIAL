class Account:
    def __init__(self, balance):
        self.__balance = balance      # private-style attribute

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount


a = Account(1000)
a.deposit(500)
print(a.get_balance())    # 1500
# print(a.__balance)      # AttributeError