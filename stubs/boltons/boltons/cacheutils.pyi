from _typeshed import Incomplete, Self, SupportsItems, SupportsKeysAndGetItem
from collections.abc import Callable, Generator, Hashable, Iterable, Iterator, Mapping
from typing import Any, Generic, TypeVar, overload
import weakref

_KT = TypeVar("_KT")
_VT = TypeVar("_VT")
_T = TypeVar("_T")

PREV: int
NEXT: int
KEY: int
VALUE: int
DEFAULT_MAX_SIZE: int

class LRI(dict[_KT, _VT]):
    hit_count: int
    miss_count: int
    soft_miss_count: int
    max_size: int
    on_miss: Callable[[_KT], _VT]
    def __init__(self, max_size: int = ..., values: Incomplete | None = ..., on_miss: Incomplete | None = ...) -> None: ...
    def __setitem__(self, key: _KT, value: _VT) -> None: ...
    def __getitem__(self, key: _KT) -> _VT: ...
    @overload
    def get(self, key: _KT, default: None = None) -> _VT | None: ...
    @overload
    def get(self, key: _KT, default: _T) -> _T | _VT: ...
    def __delitem__(self, key: _KT) -> None: ...
    @overload
    def pop(self, key: _KT) -> _VT: ...
    @overload
    def pop(self, key: _KT, default: _T) -> _T | _VT: ...
    def popitem(self) -> tuple[_KT, _VT]: ...
    def clear(self) -> None: ...
    def copy(self: Self) -> Self: ...
    @overload
    def setdefault(self, key: _KT, default: None = None) -> _VT: ...
    @overload
    def setdefault(self, key: _KT, default: _VT) -> _VT: ...
    def update(self, E: SupportsKeysAndGetItem[_KT, _VT] | Iterable[tuple[_KT, _VT]], **F: _VT) -> None: ...  # type: ignore[override]

class LRU(LRI[_KT, _VT]):
    def __getitem__(self, key: _KT) -> _VT: ...

def make_cache_key(
    args: Iterable[Hashable],
    kwargs: SupportsItems[Hashable, Hashable],
    typed: bool = False,
    kwarg_mark: object = ...,
    fasttypes: frozenset[type] = ...,
): ...

class CachedFunction:
    func: Incomplete
    get_cache: Incomplete
    scoped: Incomplete
    typed: Incomplete
    key_func: Incomplete
    def __init__(self, func, cache, scoped: bool = True, typed: bool = False, key: Incomplete | None = ...): ...
    def __call__(self, *args, **kwargs): ...

class CachedMethod:
    func: Incomplete
    get_cache: Incomplete
    scoped: Incomplete
    typed: Incomplete
    key_func: Incomplete
    bound_to: Incomplete
    def __init__(self, func, cache, scoped: bool = True, typed: bool = False, key: Incomplete | None = ...): ...
    def __get__(self, obj, objtype: Incomplete | None = ...): ...
    def __call__(self, *args, **kwargs): ...

def cached(cache: Mapping[Any, Any], scoped: bool = ..., typed: bool = ..., key: Incomplete | None = ...): ...
def cachedmethod(cache, scoped: bool = ..., typed: bool = ..., key: Incomplete | None = ...): ...

class cachedproperty(Generic[_T]):
    func: Callable[[Incomplete], _T]
    def __init__(self, func: Callable[[Incomplete], _T]) -> None: ...
    def __get__(self, obj: _T, objtype: type | None = ...): ...

class ThresholdCounter(Generic[_T]):
    total: int
    def __init__(self, threshold: float = ...) -> None: ...
    @property
    def threshold(self) -> float: ...
    def add(self, key: _T) -> None: ...
    def elements(self) -> Iterator[_T]: ...
    def most_common(self, n: int | None = ...) -> list[tuple[_T, int]]: ...
    def get_common_count(self) -> int: ...
    def get_uncommon_count(self) -> int: ...
    def get_commonality(self) -> float: ...
    def __getitem__(self, key: _T) -> int: ...
    def __len__(self) -> int: ...
    def __contains__(self, key: _T) -> bool: ...
    def iterkeys(self) -> Iterator[_T]: ...
    def keys(self) -> list[_T]: ...
    def itervalues(self) -> Generator[int, None, None]: ...
    def values(self) -> list[int]: ...
    def iteritems(self) -> Generator[tuple[_T, int], None, None]: ...
    def items(self) -> list[tuple[_T, int]]: ...
    def get(self, key: _T, default: int = ...) -> int: ...
    def update(self, iterable: Iterable[_T] | Mapping[_T, int], **kwargs: Iterable[_T] | Mapping[_T, int]) -> None: ...

class MinIDMap(Generic[_T]):
    mapping: weakref.WeakKeyDictionary[_T, int]
    ref_map: dict[_T, int]
    free: list[int]
    def __init__(self) -> None: ...
    def get(self, a: _T) -> int: ...
    def drop(self, a: _T) -> None: ...
    def __contains__(self, a: _T) -> bool: ...
    def __iter__(self) -> Iterator[_T]: ...
    def __len__(self) -> int: ...
    def iteritems(self) -> Iterator[tuple[_T, int]]: ...
