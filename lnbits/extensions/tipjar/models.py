import json
from lnurl import Lnurl, LnurlWithdrawResponse, encode as lnurl_encode  # type: ignore
from urllib.parse import urlparse, urlunparse, parse_qs, urlencode, ParseResult
from lnurl.types import LnurlPayMetadata  # type: ignore
from sqlite3 import Row
from typing import NamedTuple, Optional, Dict
import shortuuid  # type: ignore
from fastapi.param_functions import Query
from pydantic.main import BaseModel
from pydantic import BaseModel
from typing import Optional, NamedTuple
from fastapi import FastAPI, Request


class createTip(BaseModel):
    id: str
    wallet: str
    sats: int
    tipjar: int
    name: str = "Anonymous"
    message: str = ""


class Tip(NamedTuple):
    """A Tip represents a single donation"""

    id: str  # This ID always corresponds to a satspay charge ID
    wallet: str
    name: str  # Name of the donor
    message: str  # Donation message
    sats: int
    tipjar: int  # The ID of the corresponding tip jar

    @classmethod
    def from_row(cls, row: Row) -> "Tip":
        return cls(**dict(row))


class createTipJar(BaseModel):
    name: str
    wallet: str
    webhook: str = None
    onchain: str = None


class createTips(BaseModel):
    name: str
    sats: str
    tipjar: str
    message: str


class TipJar(NamedTuple):
    """A TipJar represents a user's tip jar"""

    id: int
    name: str  # The name of the donatee
    wallet: str  # Lightning wallet
    onchain: Optional[str]  # Watchonly wallet
    webhook: Optional[str]  # URL to POST tips to

    @classmethod
    def from_row(cls, row: Row) -> "TipJar":
        return cls(**dict(row))
