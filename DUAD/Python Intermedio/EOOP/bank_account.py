class BankAccount:
    def __init__(self, balance):
        self.balance = balance
    
    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"Deposited {amount}. New balance: {self.balance}")
    
    def withdraw(self, amount):
        self.balance = self.balance - amount
        print(f"Withdraw {amount}. New balance: {self.balance}")


class SavingsAccount(BankAccount):
    def __init__(self, balance, min_balance):
        super().__init__(balance)
        self.min_balance = min_balance
    
    def withdraw(self, amount):
        if self.balance - amount < self.min_balance:
            print("Error: withdrawal would go below minimum balance")
        else:
            self.balance = self.balance - amount
            print(f"Withdraw {amount}. New balance: {self.balance}")


# Test
print("--- Bank Account ---")
account = BankAccount(100)
account.deposit(50)
account.withdraw(30)

print("--- Savings Account ---")
savings = SavingsAccount(100, 50)
savings.deposit(20)
savings.withdraw(30)
savings.withdraw(50)