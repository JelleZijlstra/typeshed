import queue
import sys
import threading
from _typeshed import Self, SupportsKeysAndGetItem, SupportsRichComparison, SupportsRichComparisonT
from collections.abc import Callable, Iterable, Iterator, Mapping, MutableMapping, MutableSequence, Sequence
from types import TracebackType
from typing import Any, AnyStr, ClassVar, Generic, TypeVar, overload
from typing_extensions import SupportsIndex, TypeAlias

from .connection import Connection
from .context import BaseContext

if sys.version_info >= (3, 8):
    from .shared_memory import _SLT, ShareableList as _ShareableList, SharedMemory as _SharedMemory

    __all__ = ["BaseManager", "SyncManager", "BaseProxy", "Token", "SharedMemoryManager"]

else:
    __all__ = ["BaseManager", "SyncManager", "BaseProxy", "Token"]

if sys.version_info >= (3, 9):
    from types import GenericAlias

_T = TypeVar("_T")
_KT = TypeVar("_KT")
_VT = TypeVar("_VT")

class Namespace:
    def __init__(self, **kwds: Any) -> None: ...
    def __getattr__(self, __name: str) -> Any: ...
    def __setattr__(self, __name: str, __value: Any) -> None: ...

_Namespace: TypeAlias = Namespace

class Token:
    typeid: str | bytes | None
    address: tuple[str | bytes, int]
    id: str | bytes | int | None
    def __init__(self, typeid: bytes | str | None, address: tuple[str | bytes, int], id: str | bytes | int | None) -> None: ...
    def __getstate__(self) -> tuple[str | bytes | None, tuple[str | bytes, int], str | bytes | int | None]: ...
    def __setstate__(self, state: tuple[str | bytes | None, tuple[str | bytes, int], str | bytes | int | None]) -> None: ...

class BaseProxy:
    _address_to_local: dict[Any, Any]
    _mutex: Any
    def __init__(
        self,
        token: Any,
        serializer: str,
        manager: Any = None,
        authkey: AnyStr | None = None,
        exposed: Any = None,
        incref: bool = True,
        manager_owned: bool = False,
    ) -> None: ...
    def __deepcopy__(self, memo: Any | None) -> Any: ...
    def _callmethod(self, methodname: str, args: tuple[Any, ...] = ..., kwds: dict[Any, Any] = ...) -> None: ...
    def _getvalue(self) -> Any: ...
    def __reduce__(self) -> tuple[Any, tuple[Any, Any, str, dict[Any, Any]]]: ...

class ValueProxy(BaseProxy, Generic[_T]):
    def get(self) -> _T: ...
    def set(self, value: _T) -> None: ...
    value: _T
    if sys.version_info >= (3, 9):
        def __class_getitem__(cls, item: Any) -> GenericAlias: ...

class DictProxy(BaseProxy, MutableMapping[_KT, _VT]):
    __builtins__: ClassVar[dict[str, Any]]
    def __len__(self) -> int: ...
    def __getitem__(self, __key: _KT) -> _VT: ...
    def __setitem__(self, __key: _KT, __value: _VT) -> None: ...
    def __delitem__(self, __key: _KT) -> None: ...
    def __iter__(self) -> Iterator[_KT]: ...
    def copy(self) -> dict[_KT, _VT]: ...
    @overload
    def get(self, __key: _KT) -> _VT | None: ...
    @overload
    def get(self, __key: _KT, __default: _VT | _T) -> _VT | _T: ...
    @overload
    def pop(self, __key: _KT) -> _VT: ...
    @overload
    def pop(self, __key: _KT, __default: _VT | _T) -> _VT | _T: ...
    def keys(self) -> list[_KT]: ...  # type: ignore[override]
    def items(self) -> list[tuple[_KT, _VT]]: ...  # type: ignore[override]
    def values(self) -> list[_VT]: ...  # type: ignore[override]

class BaseListProxy(BaseProxy, MutableSequence[_T]):
    __builtins__: ClassVar[dict[str, Any]]
    def __len__(self) -> int: ...
    def __add__(self, __x: list[_T]) -> list[_T]: ...
    def __delitem__(self, __i: SupportsIndex | slice) -> None: ...
    @overload
    def __getitem__(self, __i: SupportsIndex) -> _T: ...
    @overload
    def __getitem__(self, __s: slice) -> list[_T]: ...
    @overload
    def __setitem__(self, __i: SupportsIndex, __o: _T) -> None: ...
    @overload
    def __setitem__(self, __s: slice, __o: Iterable[_T]) -> None: ...
    def __mul__(self, __n: SupportsIndex) -> list[_T]: ...
    def __rmul__(self, __n: SupportsIndex) -> list[_T]: ...
    def __reversed__(self) -> Iterator[_T]: ...
    def append(self, __object: _T) -> None: ...
    def extend(self, __iterable: Iterable[_T]) -> None: ...
    def pop(self, __index: SupportsIndex = ...) -> _T: ...
    def index(self, __value: _T, __start: SupportsIndex = ..., __stop: SupportsIndex = ...) -> int: ...
    def count(self, __value: _T) -> int: ...
    def insert(self, __index: SupportsIndex, __object: _T) -> None: ...
    def remove(self, __value: _T) -> None: ...
    # Use BaseListProxy[SupportsRichComparisonT] for the first overload rather than [SupportsRichComparison]
    # to work around invariance
    @overload
    def sort(self: BaseListProxy[SupportsRichComparisonT], *, key: None = ..., reverse: bool = ...) -> None: ...
    @overload
    def sort(self, *, key: Callable[[_T], SupportsRichComparison], reverse: bool = ...) -> None: ...

class ListProxy(BaseListProxy[_T]):
    def __iadd__(self: Self, __x: Iterable[_T]) -> Self: ...  # type: ignore[override]
    def __imul__(self: Self, __n: SupportsIndex) -> Self: ...  # type: ignore[override]

# Returned by BaseManager.get_server()
class Server:
    address: Any
    def __init__(
        self, registry: dict[str, tuple[Callable[..., Any], Any, Any, Any]], address: Any, authkey: bytes, serializer: str
    ) -> None: ...
    def serve_forever(self) -> None: ...
    def accept_connection(self, c: Connection, name: str) -> None: ...

class BaseManager:
    if sys.version_info >= (3, 11):
        def __init__(
            self,
            address: Any | None = ...,
            authkey: bytes | None = ...,
            serializer: str = ...,
            ctx: BaseContext | None = ...,
            *,
            shutdown_timeout: float = ...,
        ) -> None: ...
    else:
        def __init__(
            self, address: Any | None = ..., authkey: bytes | None = ..., serializer: str = ..., ctx: BaseContext | None = ...
        ) -> None: ...

    def get_server(self) -> Server: ...
    def connect(self) -> None: ...
    def start(self, initializer: Callable[..., object] | None = None, initargs: Iterable[Any] = ...) -> None: ...
    def shutdown(self) -> None: ...  # only available after start() was called
    def join(self, timeout: float | None = None) -> None: ...  # undocumented
    @property
    def address(self) -> Any: ...
    @classmethod
    def register(
        cls,
        typeid: str,
        callable: Callable[..., object] | None = None,
        proxytype: Any = None,
        exposed: Sequence[str] | None = None,
        method_to_typeid: Mapping[str, str] | None = None,
        create_method: bool = True,
    ) -> None: ...
    def __enter__(self: Self) -> Self: ...
    def __exit__(
        self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None
    ) -> None: ...

class SyncManager(BaseManager):
    def BoundedSemaphore(self, value: Any = ...) -> threading.BoundedSemaphore: ...
    def Condition(self, lock: Any = ...) -> threading.Condition: ...
    def Event(self) -> threading.Event: ...
    def Lock(self) -> threading.Lock: ...
    def Namespace(self) -> _Namespace: ...
    def Queue(self, maxsize: int = ...) -> queue.Queue[Any]: ...
    def RLock(self) -> threading.RLock: ...
    def Semaphore(self, value: Any = ...) -> threading.Semaphore: ...
    def Array(self, typecode: Any, sequence: Sequence[_T]) -> Sequence[_T]: ...
    def Value(self, typecode: Any, value: _T) -> ValueProxy[_T]: ...
    # Overloads are copied from builtins.dict.__init__
    @overload
    def dict(self) -> DictProxy[Any, Any]: ...
    @overload
    def dict(self, **kwargs: _VT) -> DictProxy[str, _VT]: ...
    @overload
    def dict(self, __map: SupportsKeysAndGetItem[_KT, _VT]) -> DictProxy[_KT, _VT]: ...
    @overload
    def dict(self, __map: SupportsKeysAndGetItem[str, _VT], **kwargs: _VT) -> DictProxy[str, _VT]: ...
    @overload
    def dict(self, __iterable: Iterable[tuple[_KT, _VT]]) -> DictProxy[_KT, _VT]: ...
    @overload
    def dict(self, __iterable: Iterable[tuple[str, _VT]], **kwargs: _VT) -> DictProxy[str, _VT]: ...
    @overload
    def dict(self, __iterable: Iterable[list[str]]) -> DictProxy[str, str]: ...
    @overload
    def list(self, __sequence: Sequence[_T]) -> ListProxy[_T]: ...
    @overload
    def list(self) -> ListProxy[Any]: ...

class RemoteError(Exception): ...

if sys.version_info >= (3, 8):
    class SharedMemoryServer(Server): ...

    class SharedMemoryManager(BaseManager):
        def get_server(self) -> SharedMemoryServer: ...
        def SharedMemory(self, size: int) -> _SharedMemory: ...
        def ShareableList(self, sequence: Iterable[_SLT] | None) -> _ShareableList[_SLT]: ...
