import abc

class ReversibleProxy: ...

class StartableContext(abc.ABC, metaclass=abc.ABCMeta):
    @abc.abstractmethod
    async def start(self, is_ctxmanager: bool = ...): ...
    def __await__(self): ...
    async def __aenter__(self): ...
    @abc.abstractmethod
    async def __aexit__(self, type_, value, traceback): ...

class ProxyComparable(ReversibleProxy):
    def __hash__(self) -> int: ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
