from ..backends._asn1 import (
    rsa_private_key_pkcs1_to_pkcs8 as rsa_private_key_pkcs1_to_pkcs8,
    rsa_private_key_pkcs8_to_pkcs1 as rsa_private_key_pkcs8_to_pkcs1,
    rsa_public_key_pkcs1_to_pkcs8 as rsa_public_key_pkcs1_to_pkcs8,
)
from ..backends.base import Key as Key
from ..constants import ALGORITHMS as ALGORITHMS
from ..exceptions import JWEError as JWEError, JWKError as JWKError
from ..utils import base64_to_long as base64_to_long, long_to_base64 as long_to_base64
from typing import Any

LEGACY_INVALID_PKCS8_RSA_HEADER: Any
ASN1_SEQUENCE_ID: Any
RSA_ENCRYPTION_ASN1_OID: str

def __getattr__(name: str) -> Any: ...  # incomplete
