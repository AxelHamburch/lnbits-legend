from sqlite3 import Row

from pydantic import BaseModel

class CreateLnurlPayoutData(BaseModel):
    wallet: str
    lnurlpay: str
    threshold: int

class lnurlpayout(BaseModel):
    id: str
    wallet: str
    lnurlpay: str
    threshold: str
