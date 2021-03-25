from pydantic import BaseModel

class WalletModel(BaseModel):
    wid: str
    balance: float
    wallet_type: str