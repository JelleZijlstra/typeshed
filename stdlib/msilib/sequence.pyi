import sys
from typing_extensions import TypeAlias

if sys.platform == "win32":
    _SequenceType: TypeAlias = list[tuple[str, str | None, int]]

    AdminExecuteSequence: _SequenceType
    AdminUISequence: _SequenceType
    AdvtExecuteSequence: _SequenceType
    InstallExecuteSequence: _SequenceType
    InstallUISequence: _SequenceType

    tables: list[str]
