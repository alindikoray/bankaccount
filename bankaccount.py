class BankAccount(object): #class bank account encapsulates the objects in the statement
    def __init__(self, initial_balance=0):#instance function to show the accounts initial balance
        self.balance = initial_balance
    def deposit(self, amount):#instance function for depositing to account
        self.balance += amount
    def withdraw(self, amount):
        self.balance -= amount
    def overdrawn(self):
        return self.balance < 0
my_account = BankAccount(15) #passes parameter to qualify if a withdrawal is permitted
my_account.withdraw(5)
print my_account.balance