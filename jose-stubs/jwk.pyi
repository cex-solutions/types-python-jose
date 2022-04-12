from .backends.base import Key as Key
from .constants import ALGORITHMS as ALGORITHMS
from .exceptions import JWKError as JWKError
from typing import Any, Optional, Literal

def get_key(algorithm: str) -> Optional[Key]: ...
def register_key(algorithm: str, key_class: Key) -> Literal[True]: ...
def construct(key_data: dict[str, Any], algorithm: Optional[str] = ...) -> Key: ...