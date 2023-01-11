from collections.abc import Iterator

__all__ = ["Charset", "add_alias", "add_charset", "add_codec"]

QP: int  # undocumented
BASE64: int  # undocumented
SHORTEST: int  # undocumented

class Charset:
    input_charset: str
    header_encoding: int
    body_encoding: int
    output_charset: str | None
    input_codec: str | None
    output_codec: str | None
    def __init__(self, input_charset: str = ...) -> None: ...
    def get_body_encoding(self) -> str: ...
    def get_output_charset(self) -> str | None: ...
    def header_encode(self, string: str) -> str: ...
    def header_encode_lines(self, string: str, maxlengths: Iterator[int]) -> list[str]: ...
    def body_encode(self, string: str) -> str: ...
    def __eq__(self, other: object) -> bool: ...
    def __ne__(self, __other: object) -> bool: ...

def add_charset(
    charset: str, header_enc: int | None = None, body_enc: int | None = None, output_charset: str | None = None
) -> None: ...
def add_alias(alias: str, canonical: str) -> None: ...
def add_codec(charset: str, codecname: str) -> None: ...
