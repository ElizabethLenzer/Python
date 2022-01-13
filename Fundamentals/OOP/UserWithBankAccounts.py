class BankAccount:
    all_accounts = []
    def __init__(self, int_rate, balance=0):
        self.interest=int_rate
        self.balance=balance
        BankAccount.all_accounts.append(self)
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        self.balance -= amount
        return self
    def display_account_info(self):
        print(f"balance: {self.balance}")
        return self
    def yield_interest(self):
        self.balance += (self.balance * self.interest)
        return self
    @classmethod
    def all_balances(cls):
        for account in cls.all_accounts:
            account.display_account_info()

Account1=BankAccount(.08, 1000)
Account2=BankAccount(.15, 1000)

Account1.display_account_info()
Account2.display_account_info()

Account1.deposit(250).deposit(150).deposit(600).withdraw(500).yield_interest().display_account_info()
Account2.deposit(100).deposit(2800).withdraw(750).withdraw(250).withdraw(100).withdraw(200).yield_interest().display_account_info()

print("="*80)
BankAccount.all_balances()