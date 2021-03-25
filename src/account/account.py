
class Account:
    def __init__(self):
        self.aid = None
        self.wallets = []

    def __repr__(self):
        return (
            f'Account('
            f'aid: {self.aid}, '
            f'wallets: {self.wallets})'
        )