# OOP

''' programm of a bank, a user can:
- deposite money
- withdraw money
- check his balance
'''

class Bank:
    '''this is bank account system'''

    # intilizer : contructor
    # self : this
    def __init__(self,balance=0,name=""):
        self.name = name
        self.balance = balance
        print('Your account is created.')

    def deposite(self,amount):
        self.balance += amount
        return self.balance

    def withdraw(self,amount):
        self.balance -= amount
        return self.balance
    
    def check_balance(self):
        return self.balance
    
    def __str__(self):
        return f"This bank account for {self.name} has a balance of {self.balance}"
    
    def __repr__(self): #representation
        return f"This bank account for {self.name} has a balance of {self.balance}"
    

abd_account = Bank()
print("Abed balance",abd_account.check_balance())

ahmad_account = Bank(100,"Ahmad")
ahmad_account.withdraw(10)
print(ahmad_account.check_balance())
print(ahmad_account)