# TODO: DONE!

from collections.abc import Generator
from typing import IO, Any, AnyStr, NoReturn

def reverse_iter_lines(
    file_obj: IO[AnyStr], blocksize: int = ..., preseek: bool = ..., encoding: AnyStr | None = ...
) -> Generator[AnyStr, None, None]: ...

class JSONLIterator:
    ignore_errors: bool
    def __init__(
        self, file_obj: IO[AnyStr], ignore_errors: bool = ..., reverse: bool = ..., rel_seek: float | None = ...
    ) -> None: ...
    @property
    def cur_byte_pos(self) -> int: ...
    def __iter__(self) -> NoReturn: ...
    def next(self) -> Any | NoReturn: ...
    __next__: Any | NoReturn
