from collections.abc import Iterable

__all__ = [
    "body_decode",
    "body_encode",
    "body_length",
    "decode",
    "decodestring",
    "header_decode",
    "header_encode",
    "header_length",
    "quote",
    "unquote",
]

def header_check(octet: int) -> bool: ...
def body_check(octet: int) -> bool: ...
def header_length(bytearray: Iterable[int]) -> int: ...
def body_length(bytearray: Iterable[int]) -> int: ...
def unquote(s: str | bytes | bytearray) -> str: ...
def quote(c: str | bytes | bytearray) -> str: ...
def header_encode(header_bytes: bytes | bytearray, charset: str = 'iso-8859-1') -> str: ...
def body_encode(body: str, maxlinelen: int = 76, eol: str = '\n') -> str: ...
def decode(encoded: str, eol: str = '\n') -> str: ...
def header_decode(s: str) -> str: ...

body_decode = decode
decodestring = decode
