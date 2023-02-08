import sys
import types
from _socket import _Address, _RetAddress
from _typeshed import ReadableBuffer, Self
from collections.abc import Callable
from socket import socket as _socket
from typing import Any, BinaryIO, ClassVar
from typing_extensions import TypeAlias

__all__ = [
    "BaseServer",
    "TCPServer",
    "UDPServer",
    "ThreadingUDPServer",
    "ThreadingTCPServer",
    "BaseRequestHandler",
    "StreamRequestHandler",
    "DatagramRequestHandler",
    "ThreadingMixIn",
]
if sys.platform != "win32":
    __all__ += [
        "ForkingMixIn",
        "ForkingTCPServer",
        "ForkingUDPServer",
        "ThreadingUnixDatagramServer",
        "ThreadingUnixStreamServer",
        "UnixDatagramServer",
        "UnixStreamServer",
    ]

_RequestType: TypeAlias = _socket | tuple[bytes, _socket]
_AfUnixAddress: TypeAlias = str | ReadableBuffer  # adddress acceptable for an AF_UNIX socket
_AfInetAddress: TypeAlias = tuple[str | bytes | bytearray, int]  # address acceptable for an AF_INET socket

# This can possibly be generic at some point:
class BaseServer:
    address_family: int
    server_address: _Address
    socket: _socket
    allow_reuse_address: bool
    request_queue_size: int
    socket_type: int
    timeout: float | None
    def __init__(
        self: Self, server_address: _Address, RequestHandlerClass: Callable[[Any, _RetAddress, Self], BaseRequestHandler]
    ) -> None: ...
    # It is not actually a `@property`, but we need a `Self` type:
    @property
    def RequestHandlerClass(self: Self) -> Callable[[Any, _RetAddress, Self], BaseRequestHandler]: ...
    @RequestHandlerClass.setter
    def RequestHandlerClass(self: Self, val: Callable[[Any, _RetAddress, Self], BaseRequestHandler]) -> None: ...
    def fileno(self) -> int: ...
    def handle_request(self) -> None: ...
    def serve_forever(self, poll_interval: float = 0.5) -> None: ...
    def shutdown(self) -> None: ...
    def server_close(self) -> None: ...
    def finish_request(self, request: _RequestType, client_address: _RetAddress) -> None: ...
    def get_request(self) -> tuple[Any, Any]: ...
    def handle_error(self, request: _RequestType, client_address: _RetAddress) -> None: ...
    def handle_timeout(self) -> None: ...
    def process_request(self, request: _RequestType, client_address: _RetAddress) -> None: ...
    def server_activate(self) -> None: ...
    def server_bind(self) -> None: ...
    def verify_request(self, request: _RequestType, client_address: _RetAddress) -> bool: ...
    def __enter__(self: Self) -> Self: ...
    def __exit__(
        self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: types.TracebackType | None
    ) -> None: ...
    def service_actions(self) -> None: ...
    def shutdown_request(self, request: _RequestType) -> None: ...  # undocumented
    def close_request(self, request: _RequestType) -> None: ...  # undocumented

class TCPServer(BaseServer):
    if sys.version_info >= (3, 11):
        allow_reuse_port: bool
    server_address: _AfInetAddress  # type: ignore[assignment]
    def __init__(
        self: Self,
        server_address: _AfInetAddress,
        RequestHandlerClass: Callable[[Any, _RetAddress, Self], BaseRequestHandler],
        bind_and_activate: bool = True,
    ) -> None: ...
    def get_request(self) -> tuple[_socket, _RetAddress]: ...

class UDPServer(TCPServer):
    max_packet_size: ClassVar[int]
    def get_request(self) -> tuple[tuple[bytes, _socket], _RetAddress]: ...  # type: ignore[override]

if sys.platform != "win32":
    class UnixStreamServer(BaseServer):
        server_address: _AfUnixAddress  # type: ignore[assignment]
        def __init__(
            self: Self,
            server_address: _AfUnixAddress,
            RequestHandlerClass: Callable[[Any, _RetAddress, Self], BaseRequestHandler],
            bind_and_activate: bool = True,
        ) -> None: ...

    class UnixDatagramServer(BaseServer):
        server_address: _AfUnixAddress  # type: ignore[assignment]
        def __init__(
            self: Self,
            server_address: _AfUnixAddress,
            RequestHandlerClass: Callable[[Any, _RetAddress, Self], BaseRequestHandler],
            bind_and_activate: bool = True,
        ) -> None: ...

if sys.platform != "win32":
    class ForkingMixIn:
        timeout: float | None  # undocumented
        active_children: set[int] | None  # undocumented
        max_children: int  # undocumented
        block_on_close: bool
        def collect_children(self, *, blocking: bool = False) -> None: ...  # undocumented
        def handle_timeout(self) -> None: ...  # undocumented
        def service_actions(self) -> None: ...  # undocumented
        def process_request(self, request: _RequestType, client_address: _RetAddress) -> None: ...
        def server_close(self) -> None: ...

class ThreadingMixIn:
    daemon_threads: bool
    block_on_close: bool
    def process_request_thread(self, request: _RequestType, client_address: _RetAddress) -> None: ...  # undocumented
    def process_request(self, request: _RequestType, client_address: _RetAddress) -> None: ...
    def server_close(self) -> None: ...

if sys.platform != "win32":
    class ForkingTCPServer(ForkingMixIn, TCPServer): ...
    class ForkingUDPServer(ForkingMixIn, UDPServer): ...

class ThreadingTCPServer(ThreadingMixIn, TCPServer): ...
class ThreadingUDPServer(ThreadingMixIn, UDPServer): ...

if sys.platform != "win32":
    class ThreadingUnixStreamServer(ThreadingMixIn, UnixStreamServer): ...
    class ThreadingUnixDatagramServer(ThreadingMixIn, UnixDatagramServer): ...

class BaseRequestHandler:
    # `request` is technically of type _RequestType,
    # but there are some concerns that having a union here would cause
    # too much inconvenience to people using it (see
    # https://github.com/python/typeshed/pull/384#issuecomment-234649696)
    #
    # Note also that _RetAddress is also just an alias for `Any`
    request: Any
    client_address: _RetAddress
    server: BaseServer
    def __init__(self, request: _RequestType, client_address: _RetAddress, server: BaseServer) -> None: ...
    def setup(self) -> None: ...
    def handle(self) -> None: ...
    def finish(self) -> None: ...

class StreamRequestHandler(BaseRequestHandler):
    rbufsize: ClassVar[int]  # undocumented
    wbufsize: ClassVar[int]  # undocumented
    timeout: ClassVar[float | None]  # undocumented
    disable_nagle_algorithm: ClassVar[bool]  # undocumented
    connection: Any  # undocumented
    rfile: BinaryIO
    wfile: BinaryIO

class DatagramRequestHandler(BaseRequestHandler):
    packet: _socket  # undocumented
    socket: _socket  # undocumented
    rfile: BinaryIO
    wfile: BinaryIO
