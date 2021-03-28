
class Account:
    def __init__(self):
        self.aid = None
        self.wallets = []
        self.total_balance = None


    def __repr__(self):
        return (
            f'Account('
            f'aid: {self.aid}, '
            f'wallets: {self.wallets}, '
            f'total_balance: {self.total_balance})'
        )