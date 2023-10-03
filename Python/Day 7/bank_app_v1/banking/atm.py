
from utils.input import read_value

class ATM(): #ATM is NOT a type of BankAccount
    def __init__(self, bank):
        self._bank=bank
        self._keyboard=read_value
        
    def start(self):
        print('ATM Menu')
        self._account_number= self._keyboard('Account Number?',int)
        self._password= self._keyboard('Password?')
        self._user_menu()

    def _user_menu(self):
        while True:
            choice=self._keyboard('1.Deposit\t2.Withdraw\t3.Check Balance\t4. Transfer\t0.Exit\nChoose:',int)
            

    def _dispense_cash(self, amount):
        print(f'Please take your cash {amount}')

    def _show_message(self,message):
        print(message)



