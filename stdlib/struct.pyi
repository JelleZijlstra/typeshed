from _typeshed import ReadableBuffer, WriteableBuffer
from collections.abc import Iterator
from typing import Any

__all__ = ["calcsize", "pack", "pack_into", "unpack", "unpack_from", "iter_unpack", "Struct", "error"]

class error(Exception): ...

def pack(__fmt: str | bytes, *v: Any) -> bytes: ...
def pack_into(__fmt: str | bytes, __buffer: WriteableBuffer, __offset: int, *v: Any) -> None: ...
def unpack(__format: str | bytes, __buffer: ReadableBuffer) -> tuple[Any, ...]: ...
def unpack_from(__format: str | bytes, buffer: ReadableBuffer, offset: int = 0) -> tuple[Any, ...]: ...
def iter_unpack(__format: str | bytes, __buffer: ReadableBuffer) -> Iterator[tuple[Any, ...]]: ...
def calcsize(__format: str | bytes) -> int: ...

class Struct:
    @property
    def format(self) -> str: ...
    @property
    def size(self) -> int: ...
    def __init__(self, format: str | bytes) -> None: ...
    def pack(self, *v: Any) -> bytes: ...
    def pack_into(self, buffer: WriteableBuffer, offset: int, *v: Any) -> None: ...
    def unpack(self, __buffer: ReadableBuffer) -> tuple[Any, ...]: ...
    def unpack_from(self, buffer: ReadableBuffer, offset: int = ...) -> tuple[Any, ...]: ...
    def iter_unpack(self, __buffer: ReadableBuffer) -> Iterator[tuple[Any, ...]]: ...
