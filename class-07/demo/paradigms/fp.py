# Functional Programming

''' programm of a bank, a user can:
- deposite money
- withdraw money
- check his balance
'''
def deposite(balance, amount):
    return balance + amount

def withdraw(balance, amount):
    return balance - amount

def check_balance(balance):
    return balance

ahmad_balance = 100
ahmad_balance = withdraw(ahmad_balance, 50)
print(check_balance(ahmad_balance))

'''
in this examle, data and all functions are related to each other
when any fucntio is excuted, the data (balance) affected
in this case, it is better to use OOP paradigm
'''
