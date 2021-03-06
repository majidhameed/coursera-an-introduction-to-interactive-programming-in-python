class BankAccount:
    def __init__(self, initial_balance=0):
        """Creates an account with the given balance."""
        self.balance=initial_balance
        self.fees = 0
        
    def deposit(self, amount):
        """Deposits the amount into the account."""
        self.balance += amount
        
    def withdraw(self, amount):
        """Withdraws the amount from the account.  Each withdrawal resulting in a negative balance also deducts a fee of 5 dollars from the balance."""
        if amount > self.balance:
            self.balance -= 5
            self.fees += 5
        
        self.balance -= amount
             
    def get_balance(self):
        """Returns the current balance in the account."""
        return self.balance
       
    def get_fees(self):
        """Returns the total fees ever accrued in the account."""
        return self.fees
        
my_account = BankAccount(10)
my_account.withdraw(5)
my_account.deposit(10)
my_account.withdraw(5)
my_account.withdraw(15)
my_account.deposit(20)
my_account.withdraw(5) 
my_account.deposit(10)
my_account.deposit(20)
my_account.withdraw(15)
my_account.deposit(30)
my_account.withdraw(10)
my_account.withdraw(15)
my_account.deposit(10)
my_account.withdraw(50) 
my_account.deposit(30)
my_account.withdraw(15)
my_account.deposit(10)
my_account.withdraw(5) 
my_account.deposit(20)
my_account.withdraw(15)
my_account.deposit(10)
my_account.deposit(30)
my_account.withdraw(25) 
my_account.withdraw(5)
my_account.deposit(10)
my_account.withdraw(15)
my_account.deposit(10)
my_account.withdraw(10) 
my_account.withdraw(15)
my_account.deposit(10)
my_account.deposit(30)
my_account.withdraw(25) 
my_account.withdraw(10)
my_account.deposit(20)
my_account.deposit(10)
my_account.withdraw(5) 
my_account.withdraw(15)
my_account.deposit(10)
my_account.withdraw(5) 
my_account.withdraw(15)
my_account.deposit(10)
my_account.withdraw(5) 
print my_account.get_balance(), my_account.get_fees()