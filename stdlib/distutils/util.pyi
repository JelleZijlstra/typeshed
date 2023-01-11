from _typeshed import StrPath
from collections.abc import Callable, Container, Iterable, Mapping
from typing import Any
from typing_extensions import Literal

def get_platform() -> str: ...
def convert_path(pathname: str) -> str: ...
def change_root(new_root: str, pathname: str) -> str: ...
def check_environ() -> None: ...
def subst_vars(s: str, local_vars: Mapping[str, str]) -> None: ...
def split_quoted(s: str) -> list[str]: ...
def execute(
    func: Callable[..., object], args: tuple[Any, ...], msg: str | None = None, verbose: bool = 0, dry_run: bool = 0
) -> None: ...
def strtobool(val: str) -> Literal[0, 1]: ...
def byte_compile(
    py_files: list[str],
    optimize: int = 0,
    force: bool = 0,
    prefix: str | None = None,
    base_dir: str | None = None,
    verbose: bool = 1,
    dry_run: bool = 0,
    direct: bool | None = None,
) -> None: ...
def rfc822_escape(header: str) -> str: ...
def run_2to3(
    files: Iterable[str],
    fixer_names: Iterable[str] | None = ...,
    options: Mapping[str, Any] | None = ...,
    explicit: Container[str] | None = ...,  # unused
) -> None: ...
def copydir_run_2to3(
    src: StrPath,
    dest: StrPath,
    template: str | None = ...,
    fixer_names: Iterable[str] | None = ...,
    options: Mapping[str, Any] | None = ...,
    explicit: Container[str] | None = ...,
) -> list[str]: ...

class Mixin2to3:
    fixer_names: Iterable[str] | None
    options: Mapping[str, Any] | None
    explicit: Container[str] | None
    def run_2to3(self, files: Iterable[str]) -> None: ...
