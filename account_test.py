from nose.tools import assert_equals, nottest
from abcbank.account import Account


def test_transfer():
    checking_account = Account(0)
    savings_account = Account(1)
    checking_account.deposit(100.0)
    savings_account.deposit(200.0)
    checking_account.transfer(savings_account, 50)
    assert_equals(checking_account.sumTransactions(), 50.0)
    assert_equals(savings_account.sumTransactions(), 250.0)