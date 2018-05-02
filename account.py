from abcbank.transaction import Transaction
import datetime

CHECKING = 0
SAVINGS = 1
MAXI_SAVINGS = 2


class Account:
    def __init__(self, accountType):
        self.accountType = accountType
        self.transactions = []

    def deposit(self, amount):
        if (amount <= 0):
            raise ValueError("amount must be greater than zero")
        else:
            self.transactions.append(Transaction(amount))

    def withdrawal_check(self, last_withdrawal, position):
        withdrawals_list = ["just checking position - 0", datetime.date(1990, 1, 2)]
        self.last_withdrawal = last_withdrawal
        withdrawals_list[position] = last_withdrawal
        today = datetime.date.today()
        if ((withdrawals_list[1])-today).days > 10:
            return 1
        else:
            return 0

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("amount must be greater than zero")
        else:
            self.transactions.append(Transaction(-amount))
            self.withdrawal_check(datetime.date.today(), 1)

    def interestEarned(self):

        amount = self.sumTransactions()
        if self.accountType == SAVINGS:
            if amount <= 1000:
                return amount * 0.001
            else:
                return 1 + (amount - 1000) * 0.002

        if self.accountType == MAXI_SAVINGS:
            if self.withdrawal_check((datetime.date(1990, 1, 1)), 0) is 1:
                return amount * 0.05
            else:
                return amount * 0.01

        else:
            return amount * 0.001

    def sumTransactions(self, checkAllTransactions=True):
        return sum([t.amount for t in self.transactions])

    def transfer(self, trans_to, trans_amount):
        if self.sumTransactions() >= trans_amount:
            self.withdraw(trans_amount)
            trans_to.deposit(trans_amount)
        else:
            print("Transfer exceeds current balance")
