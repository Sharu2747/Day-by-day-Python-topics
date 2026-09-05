class BankAccount:

 def __init__(self,name,balance):
   self.name=name
   self.balance=balance
   print("Starting balance:",balance)

 def deposit(self,amount):
   self.balance=self.balance+amount
   print("Deposit:",amount)

 def display_balance(self):
   print("Final amount:",self.balance)

account1=BankAccount("Sharu",5000)
account1.deposit(1000)

account1.display_balance()