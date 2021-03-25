import datetime
from pydantic import BaseModel

class UserModel(BaseModel):
    first_name: str
    middle_name: str
    last_name: str
    date_of_birth: datetime.datetime