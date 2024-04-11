class BankAccount:
    def __init__(self, account_number, owner, initial_balance=0):
        self.account_number = account_number
        self.owner = owner
        self.balance = initial_balance
        self.transactions = []

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount
        self.transactions.append(('DEPOSIT', amount))

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        self.transactions.append(('WITHDRAWAL', amount))

    def transfer(self, amount, target_account):
        if amount <= 0:
            raise ValueError("Transfer amount must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.withdraw(amount)
        target_account.deposit(amount)
        self.transactions.append(('TRANSFER', amount, target_account.account_number))
        target_account.transactions.append(('TRANSFER IN', amount, self.account_number))

    def get_balance(self):
        return self.balance

    def get_transactions(self):
        return self.transactions