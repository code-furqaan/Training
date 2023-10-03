
class Bank:
    _current_account_number = 1000000001

    def __init__(self):
        # self.__bank_name = name
        self.__accounts = list()
    
    def add_account(self, account):
        self.__accounts.append(account)

    def open_account(self, name, password, amount, account_type, interest_rate=3.5):
        account = BankAcount(name, password, amount, account_type, interest_rate)
        self.__accounts.append(account)
        return account
    
    def deposit(self, account, amount):
        account.self_balance(amount)
    
    def transfer(self, from_account, amount, password, to_account):
        if from_account.check_password(password) == False:
            print("Incorrect Password")
            return
        
    
    

class BankAcount(Bank):
    
    def __init__(self, name, password, deposit_amount, account_type, interest_rate):

        if not account_type().init_check(deposit_amount):
            print(f'Account for {name} not created - Deposit Amount too low\n')
            return
        
        self.__name = name
        self.__password = password
        self.__balance = deposit_amount
        self.__max_balance = deposit_amount
        self.__interest_rate = interest_rate

        self.__account_type = account_type()

        self.__account_number = Bank._current_account_number
        Bank._current_account_number += 1

        print(f'Account for {name} created - Account Number: {self.__account_number}\n')
        

    def check_password(self, password):
        if self.__password == password:
            return True
        return False
    
    def set_balance(self, amount):
        self.__balance+=amount
        if self.__balance > self.__max_balance:
            self.__max_balance = self.__balance




class SavingsAcount:
    def init_check(self, balance):
        if balance<5000:
            return False
        return True
    
    def check(self, balance, amount):
        if (balance - amount)<5000:
            return False
        return True

class CurrentAcount:
    def init_check(self, balance):
        if balance<0:
            return False
        return True
    
    def check(self, balance, amount):
        if (balance - amount)<0:
            return False
        return True

class OverdraftAcount:
    def init_check(self, balance):
        if balance<0:
            return False
        return True
    
    def check(balance, amount):
        if (balance + balance*0.1 - amount)<0:
            return False
        return True
    

icici = Bank() 
a1 = icici.open_account('Vivek', 'p@ss', 50000, SavingsAcount)
a2 = icici.open_account('XXXXX', 'p@ss', 50000, SavingsAcount)



