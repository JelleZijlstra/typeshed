from _typeshed import Self
from collections.abc import Iterator, MutableMapping
from types import TracebackType
from typing_extensions import TypeAlias

__all__ = ["error", "open"]

_KeyType: TypeAlias = str | bytes
_ValueType: TypeAlias = str | bytes | bytearray

error = OSError

class _Database(MutableMapping[_KeyType, bytes]):
    def __init__(self, filebasename: str, mode: str, flag: str = ...) -> None: ...
    def sync(self) -> None: ...
    def iterkeys(self) -> Iterator[bytes]: ...  # undocumented
    def close(self) -> None: ...
    def __getitem__(self, key: _KeyType) -> bytes: ...
    def __setitem__(self, key: _KeyType, val: _ValueType) -> None: ...
    def __delitem__(self, key: _KeyType) -> None: ...
    def __iter__(self) -> Iterator[bytes]: ...
    def __len__(self) -> int: ...
    def __del__(self) -> None: ...
    def __enter__(self: Self) -> Self: ...
    def __exit__(
        self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None
    ) -> None: ...

def open(file: str, flag: str = ..., mode: int = ...) -> _Database: ...
