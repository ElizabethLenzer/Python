class User:
    def __init__(self, name, age):
        self.balance=0
        self.name=name
        self.age=age
    def make_deposit(self, amount):
        self.balance += amount
        return self
    def make_withdrawal(self, amount):
        self.balance -= amount
        return self
    def display_userbalance(self):
        print(self.name,self.balance)
        return self
    def transfer_money(self, amount, user):
        user.make_deposit(amount)
        self.make_withdrawal(amount)
        return self


Person1=User('Chloe', 2)
Person2=User('Elizabeth', 23)
Person3=User('Nathan', 23)

Person1.make_deposit(5).make_deposit(20).make_deposit(100).make_withdrawal(10).display_userbalance()

Person2.make_deposit(1500).make_withdrawal(720).make_deposit(1500).make_withdrawal(384).display_userbalance()

Person3.make_deposit(6000).make_withdrawal(250).make_withdrawal(155).make_withdrawal(35).display_userbalance()

# BONUS

Person1.transfer_money(2,Person3)
Person1.display_userbalance()
Person3.display_userbalance()