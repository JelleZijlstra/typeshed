import sys
from _typeshed import ReadableBuffer
from collections.abc import Callable, Iterable
from email.message import Message
from types import TracebackType
from typing import IO, Any, BinaryIO
from typing_extensions import Self

__all__ = ["addbase", "addclosehook", "addinfo", "addinfourl"]

class addbase(BinaryIO):
    fp: IO[bytes]
    def __init__(self, fp: IO[bytes]) -> None: ...
    def __enter__(self) -> Self: ...
    def __exit__(
        self, type: type[BaseException] | None, value: BaseException | None, traceback: TracebackType | None
    ) -> None: ...
    def __iter__(self) -> Self: ...
    def __next__(self) -> bytes: ...
    def close(self) -> None: ...
    # These methods don't actually exist, but the class inherits at runtime from
    # tempfile._TemporaryFileWrapper, which uses __getattr__ to delegate to the
    # underlying file object. To satisfy the BinaryIO interface, we pretend that this
    # class has these additional methods.
    def fileno(self) -> int: ...
    def flush(self) -> None: ...
    def isatty(self) -> bool: ...
    def read(self, n: int = ...) -> bytes: ...
    def readable(self) -> bool: ...
    def readline(self, limit: int = ...) -> bytes: ...
    def readlines(self, hint: int = ...) -> list[bytes]: ...
    def seek(self, offset: int, whence: int = ...) -> int: ...
    def seekable(self) -> bool: ...
    def tell(self) -> int: ...
    def truncate(self, size: int | None = ...) -> int: ...
    def writable(self) -> bool: ...
    # https://github.com/python/mypy/issues/14002
    def write(self, s: ReadableBuffer) -> int: ...  # type: ignore[override]
    def writelines(self, lines: Iterable[bytes]) -> None: ...  # type: ignore[override]

class addclosehook(addbase):
    closehook: Callable[..., object]
    hookargs: tuple[Any, ...]
    def __init__(self, fp: IO[bytes], closehook: Callable[..., object], *hookargs: Any) -> None: ...

class addinfo(addbase):
    headers: Message
    def __init__(self, fp: IO[bytes], headers: Message) -> None: ...
    def info(self) -> Message: ...

class addinfourl(addinfo):
    url: str
    code: int | None
    if sys.version_info >= (3, 9):
        @property
        def status(self) -> int | None: ...

    def __init__(self, fp: IO[bytes], headers: Message, url: str, code: int | None = None) -> None: ...
    def geturl(self) -> str: ...
    def getcode(self) -> int | None: ...
