from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel
from pydantic import ValidationError


class User(BaseModel):
    id: int # the annotation-only declaration tells pydantic that this field is required.
    name = 'John Doe' # name is inferred as a string from the provided default; because it has a default, it is not required.
    signup_ts: Optional[datetime] = None # pydantic will process either a unix timestamp int (e.g. 1496498400) or a string representing the date & time.
    friends: List[int] = []


external_data = {
    'id': '123', #  integer-like objects will be converted to integers.
    'signup_ts': '2019-06-01 12:22',
    'friends': [1, 2, '3'],
}


user = User(**external_data)
print(user.id)
print(repr(user.signup_ts))
print(user.friends)
print(user.dict())

try:
    User(signup_ts='broken', friends=[1, 2, 'not number'])
except ValidationError as e:
    for err in e.errors():
        print(f'{err["loc"][0]} - {err["msg"]}')
