from pydantic import BaseModel

class AccountModel(BaseModel):
    aid: str
    wallets: list