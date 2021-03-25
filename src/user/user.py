from src.account.account import Account

class User:
    def __init__(self, first_name, middle_name, last_name, date_of_birth):
        self.uid = None #not implemented yet
        self.account = Account() #not implemented yet
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth

    def __repr__(self):
        return (
            f'User('
            f'uid: {self.uid}, '
            f'account_id: {self.account}, '
            f'first_name: {self.first_name}, '
            f'middle_name: {self.middle_name}, '
            f'last_name: {self.last_name}, '
            f'date_of_birth: {self.date_of_birth})'
        )



x = User('O', 'U', 'B', 1)
print(x)