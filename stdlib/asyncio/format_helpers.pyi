import functools
import traceback
from collections.abc import Iterable
from types import FrameType, FunctionType
from typing import Any, overload
from typing_extensions import TypeAlias

class _HasWrapper:
    __wrapper__: _HasWrapper | FunctionType

_FuncType: TypeAlias = FunctionType | _HasWrapper | functools.partial[Any] | functools.partialmethod[Any]

@overload
def _get_function_source(func: _FuncType) -> tuple[str, int]: ...
@overload
def _get_function_source(func: object) -> tuple[str, int] | None: ...
def _format_callback_source(func: object, args: Iterable[Any]) -> str: ...
def _format_args_and_kwargs(args: Iterable[Any], kwargs: dict[str, Any]) -> str: ...
def _format_callback(func: object, args: Iterable[Any], kwargs: dict[str, Any], suffix: str = '') -> str: ...
def extract_stack(f: FrameType | None = None, limit: int | None = None) -> traceback.StackSummary: ...
