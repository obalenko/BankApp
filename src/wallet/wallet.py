from src.wallet.card_settings import CardSettings


TYPES = [
    'DEBIT',
    'CREDIT'
]

CURRENCIES = [
    'UAH',
    'USD',
    'EUR'
]

WALLET_STATUS = [
    'ACTIVE',
    'DISABLED',
    'BLOCKED'
]

class OperationNotAllowed(Exception):
    pass


class Wallet:
    def __init__(self, type='DEBIT', currency='UAH'):
        self.wid = None
        self.type = type
        self.currency = currency
        self.balance = 0
        self.status = 'ACTIVE'
        self.negative_balance_allowed = True if self.type == 'CREDIT' else False
        self.card_settings = CardSettings()

    def __repr__(self):
        return (
            f'Wallet('
            f'wid: {self.wid}, '
            f'type: {self.type}, '
            f'status: {self.status}, '
            f'currency: {self.currency}, '
            f'balance: {self.balance}, '
            f'negative_balance: {self.negative_balance_allowed})'
        )

    @property
    def get_balance(self):
        '''
        Get wallet balance
        :return:
        '''
        return self.balance

    def add_balance(self, value):
        '''
        Add balance. To subtract just put negative value argument
        :param value:
        :return:
        '''
        self.balance += value
        if not self.negative_balance_allowed:
            raise OperationNotAllowed('Balance can not be negative for this type of card')

    def send(self):
        '''
        Send money to another user
        :return:
        '''
        raise NotImplementedError()

    def withdraw(self):
        '''
        Withdraw cash using ATM
        :return:
        '''
        raise NotImplementedError()

    def service_pay(self):
        '''
        Pay with card to one of the selected built-in service
        :return:
        '''
        raise NotImplementedError()



w = Wallet()