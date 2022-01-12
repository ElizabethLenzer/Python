class User:
    def __init__(self, name, age):
        self.balance=0
        self.name=name
        self.age=age
    def make_deposit(self, amount):
        self.balance += amount
    def make_withdrawal(self, amount):
        self.balance -= amount
    def display_userbalance(self):
        print(self.name,self.balance)
    def transfer_money(self, amount, user):
        user.make_deposit(amount)
        self.make_withdrawal(amount)


Person1=User('Chloe', 2)
Person2=User('Elizabeth', 23)
Person3=User('Nathan', 23)

Person1.make_deposit(5)
Person1.make_deposit(20)
Person1.make_deposit(100)
Person1.make_withdrawal(10)
Person1.display_userbalance()

Person2.make_deposit(1500)
Person2.make_withdrawal(720)
Person2.make_deposit(1500)
Person2.make_withdrawal(384)
Person2.display_userbalance()

Person3.make_deposit(6000)
Person3.make_withdrawal(250)
Person3.make_withdrawal(155)
Person3.make_withdrawal(35)
Person3.display_userbalance()

# BONUS

Person1.transfer_money(2,Person3)
Person1.display_userbalance()
Person3.display_userbalance()
