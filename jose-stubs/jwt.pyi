from typing import Any, Union, Optional, Iterable
from .constants import ALGORITHMS as ALGORITHMS

def encode(
    claims: dict[str, Any],
    key: Union[str, dict[str, str]],
    algorithm: str = ...,
    headers: Optional[dict[str, str]] = ...,
    access_token: Optional[str] = ...,
) -> str: ...
def decode(
    token: str,
    key: Union[str, dict[str, str]],
    algorithms: Union[str, list[str], None] = ...,
    options: Optional[dict[str, Union[str, int]]] = ...,
    audience: Optional[str] = ...,
    issuer: Union[str, Iterable[str], None] = ...,
    subject: Optional[str] = ...,
    access_token: Optional[str] = ...,
) -> dict[str, Any]: ...
def get_unverified_header(token: str) -> dict[str, str]: ...
def get_unverified_headers(token: str) -> dict[str, str]: ...
def get_unverified_claims(token: str) -> dict[str, Any]: ...
