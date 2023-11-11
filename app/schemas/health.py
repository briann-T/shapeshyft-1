from typing import Optional

from pydantic import BaseModel

from .general import Response

import datetime
import time

class wEntry(BaseModel):  
    amt: int

class wCreateResponse(Response):
    date: datetime.date

class wEntryResponse(Response):
    amt : int
    date: datetime.date
    time: datetime.datetime
    rec: str

class sEntry(BaseModel):
    date: datetime.date
    s_time: str
    e_time: str

class sEntryResponse(Response):
    date: datetime.date

class sResponse(Response):
    date: datetime.date
    s_time:  datetime.time
    e_time:  datetime.time
    h_slept: float
    rec : str
    