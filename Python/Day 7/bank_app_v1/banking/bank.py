from banking.accounts.bank_account import BankAccount

class Bank:
    def __init__(self, name,interset_rate):
        self. _name=name
        self.interst_rate=interset_rate
        self._last_id=0
        self._accounts=[]

    def open_account(self, name, password, balance):
        self._last_id+=1
        account = BankAccount(self._last_id, name, password, balance)
        self._accounts.append(account)
        return account._accountNumber
    
    def get_account(self, account_number):
        for account in self._accounts:
            if account._account_number==account_number:
                return account
        return None

    def deposit(self, account_number, amount):
        account=self.get_account(account_number)
        if account:
            return account.deposit(amount)
        else:
            return False


    def withdraw(self, account_number, amount, password):
        account=self.get_account(account_number)
        if account:
            return account.withdraw(amount)
        else:
            return False

    def transfer(self, source_account, amount, password, target_account):
        source=self.get_account(source_account)
        target=self.get_account(target_account)
        if source and target:
            if source.withdraw(amount,password):
                return target.deposit(amount)

        return False


    def credit_interst(self):
        for account in self._accounts:
            account.credit_interest(self.interst_rate)

