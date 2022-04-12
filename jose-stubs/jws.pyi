from .backends.base import Key as Key
from .constants import ALGORITHMS as ALGORITHMS
from .exceptions import JWSError as JWSError, JWSSignatureError as JWSSignatureError
from .utils import base64url_decode as base64url_decode, base64url_encode as base64url_encode
from typing import Any

def __getattr__(name: str) -> Any: ...  # incomplete
