"""
Module with defining symbol management, including Symbol Table Manager,
symbol definition, symbol types and so on.
"""

from dataclasses import dataclass
from enum import Enum
from typing import Any

class SymbolType(Enum):
    """All available symbol types."""
    VARIABLE = 0
    FUNCTION = 1

class Scope(Enum):
    """Scope of a symbol."""
    LOCAL = 0
    GLOBAL = 1

@dataclass
class Symbol:
    """Representation of a named entity such as a variable or function."""
    name: str
    type: SymbolType
    value: Any
    scope: Scope | None = None # FIXME: Implement a scope assignment mechanism.
    created_at_line: int | None = None # FIXME: Implement a line creation reading mechanism.

    def eval(self) -> Any:
        """Evaluate symbol to its value."""
        if self.type == SymbolType.VARIABLE:
            return self.value
        raise NotImplementedError


class SymbolTableManager:
    """
    Class manages symbols (named entities), such as variable or functions.
    """
    def __init__(self) -> None:
        self._symbol_table: dict[str, Symbol] = {}
        super().__init__()

    def __setitem__(self, key: object, value: object) -> None:
        if not isinstance(key, str):
            raise KeyError(
                f"Key of an element has to be of type `str`. "
                f"Received `{type(key)}`."
            )

        if not isinstance(value, Symbol):
            raise ValueError(
                f"Cannot add {value} to the Symbol Table. "
                "Only instances of Symbol may be added."
            )

        if value.name in self._symbol_table:
            self._symbol_table[value.name] = value
            raise UserWarning(
                f"Symbol with the name `{value.name}` already exists. "
                "Replacing with a new value."
            )

        self._symbol_table[value.name] = value

    def __getitem__(self, value: object) -> Symbol | None:
        if isinstance(value, str):
            return self._symbol_table.get(value, None)
        raise NotImplementedError
