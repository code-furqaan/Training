
class Bank:
    _current_account_number = 1000000001

    def __init__(self):
        # self.__bank_name = name
        self.__accounts = list()
    
    def add_account(self, account):
        self.__accounts.append(account)

    def open_account(self, name, password, amount, account_type):
        account = BankAcount(name, password, amount, account_type)
        self.__accounts.append(account)
        return account
    
    def deposit(self, account, amount):
        if account.deposit(amount):
            print('Deposit Successful')

    def withdraw(self, account, password, amount):
        if account.withdraw(amount, password):
            print('Withdrawal Successful')
        else:
            print('Withdrawal Failed')
    
    def transfer(self, from_account, password, amount, to_account):
        if from_account.check_password(password) == False:
            print("Incorrect Password")
        if from_account.withdraw(amount, password) == False:
            print('Transfer Failed')
            return
        
        to_account.deposit(amount)
    
    def credit_interest(self):
        for account in self.__accounts:
            rate = account.get_rate()
            balance = account.get_balance()
            account.deposit(balance * rate/100)
        
    
    class ATM:
        def print(self, account):

            name, account_number, account_type, balance = account.get_details()

            print('-------------------')
            print(f'Name: {name}\nBalance:{balance}')
            print('-------------------')



    

class BankAcount(Bank):
    
    def __init__(self, name, password, deposit_amount, account_type):

        if not account_type().init_check(deposit_amount):
            print(f'Account for {name} not created - Deposit Amount too low\n')
            return
        
        self.__name = name
        self.__password = password
        self.__balance = deposit_amount
        self.__max_balance = deposit_amount

        self.__account_type = account_type()

        self.__account_number = Bank._current_account_number
        Bank._current_account_number += 1

        print(f'Account for {name} created - Account Number: {self.__account_number}\n')
        

    def check_password(self, password):
        if self.__password == password:
            return True
        return False
    
    def deposit(self, amount):
        self.__balance+=amount
        if self.__balance > self.__max_balance:
            self.__max_balance = self.__balance
        return True
    
    def withdraw(self, amount, password):
        if self.check_password(password) == False:
            print("Incorrect Password")
            return False

        if self.__account_type.check(self.__balance, amount, self.__max_balance) == False:
            print("Amount greater than Allowed")
            return False
        
        self.__balance-=amount
        if(self.__balance < 0):
            self.__balance += self.__balance*0.01
        
        return True
    
    def get_balance(self):
        return self.__balance
    
    def get_details(self):
        return (self.__name, self.__account_number, self.__account_type, self.__balance)
    def get_rate(self):
        return self.__account_type.get_interest_rate()



class SavingsAcount:
    __interest_rate = 3.5
    def init_check(self, balance):
        if balance<5000:
            return False
        return True
    
    def check(self, balance, amount, max_balance):
        if (balance - amount)<5000:
            return False
        return True
    
    def get_interest_rate(self):
        return self.__interest_rate

class CurrentAcount:
    __interest_rate = 3.5
    def init_check(self, balance):
        if balance<0:
            return False
        return True
    
    def check(self, balance, amount, max_balance):
        if (balance - amount)<0:
            return False
        return True
    
    def get_interest_rate(self):
        return self.__interest_rate

class OverdraftAcount:
    __interest_rate = 3.5
    def init_check(self, balance):
        if balance<0:
            return False
        return True
    
    def check(self, balance, amount, max_balance):
        if (balance + max_balance*0.1 - amount)<0:
            return False
        return True
    
    def get_interest_rate(self):
        return self.__interest_rate
    

icici = Bank() 
icici_atm = icici.ATM()
a1 = icici.open_account('Furqan', 'p@ss', 50000, SavingsAcount)
a2 = icici.open_account('XXXXX', 'p@ss', 50000, OverdraftAcount)

icici_atm.print(a1)

icici.deposit(a1, 5000)

icici_atm.print(a1)

icici.withdraw(a1, 'p@ss',5000)

icici_atm.print(a1)

icici.transfer(a1, 'p@ss',5000, a2)

icici_atm.print(a1)

icici_atm.print(a2)

icici.withdraw(a2, 'p@ss',60000)

icici_atm.print(a2)

icici.credit_interest()

icici_atm.print(a1)

icici_atm.print(a2)




