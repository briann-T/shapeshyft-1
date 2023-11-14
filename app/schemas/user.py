from typing import Optional

from pydantic import UUID4, BaseModel, EmailStr, validator, Field


from .general import Response, Password

import datetime


class UserAccountCreateRequest(Password):
    phone_number: str
    email: Optional[EmailStr] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None


class PredictCaloriesRequest(BaseModel):
    weight: float
    height: float
    age: int

class UserAccount(BaseModel):
    uuid: UUID4
    phone_number: str
    email: Optional[EmailStr] = None

class CaloriePredictionResponse(Response):
    calories: float

class UserAccountResponse(Response):
    uuid: UUID4
    phone_number: str
    email: Optional[EmailStr] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    date_joined: datetime.datetime
    last_login: datetime.datetime
