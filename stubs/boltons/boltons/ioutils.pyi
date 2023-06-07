import abc
from _typeshed import Incomplete
from abc import abstractmethod

text_type = str
binary_type = bytes
READ_CHUNK_SIZE: int
EINVAL: Incomplete

class SpooledIOBase(metaclass=abc.ABCMeta):
    __metaclass__: Incomplete
    def __init__(self, max_size: int = ..., dir: Incomplete | None = ...) -> None: ...
    @abstractmethod
    def read(self, n: int = ...): ...
    @abstractmethod
    def write(self, s): ...
    @abstractmethod
    def seek(self, pos, mode: int = ...): ...
    @abstractmethod
    def readline(self, length: Incomplete | None = ...): ...
    @abstractmethod
    def readlines(self, sizehint: int = ...): ...
    @abstractmethod
    def rollover(self): ...
    @abstractmethod
    def tell(self): ...
    @property
    @abc.abstractmethod
    def buffer(self): ...
    @property
    @abc.abstractmethod
    def len(self): ...
    softspace: Incomplete
    def close(self): ...
    def flush(self): ...
    def isatty(self): ...
    def next(self): ...
    @property
    def closed(self): ...
    @property
    def pos(self): ...
    @property
    def buf(self): ...
    def fileno(self): ...
    def truncate(self, size: Incomplete | None = ...): ...
    def getvalue(self): ...
    def seekable(self): ...
    def readable(self): ...
    def writable(self): ...
    __next__: Incomplete
    def __len__(self): ...
    def __iter__(self): ...
    def __enter__(self): ...
    def __exit__(self, *args) -> None: ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    def __bool__(self): ...
    __nonzero__: Incomplete

class SpooledBytesIO(SpooledIOBase):
    def read(self, n: int = ...): ...
    def write(self, s) -> None: ...
    def seek(self, pos, mode: int = ...): ...
    def readline(self, length: Incomplete | None = ...): ...
    def readlines(self, sizehint: int = ...): ...
    def rollover(self) -> None: ...
    @property
    def buffer(self): ...
    @property
    def len(self): ...
    def tell(self): ...

class SpooledStringIO(SpooledIOBase):
    def __init__(self, *args, **kwargs) -> None: ...
    def read(self, n: int = ...): ...
    def write(self, s) -> None: ...
    def seek(self, pos, mode: int = ...): ...
    def readline(self, length: Incomplete | None = ...): ...
    def readlines(self, sizehint: int = ...): ...
    @property
    def buffer(self): ...
    def rollover(self) -> None: ...
    def tell(self): ...
    @property
    def len(self): ...

def is_text_fileobj(fileobj) -> bool: ...

class MultiFileReader:
    def __init__(self, *fileobjs) -> None: ...
    def read(self, amt: Incomplete | None = ...): ...
    def seek(self, offset, whence=...) -> None: ...
