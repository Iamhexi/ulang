"""Module with boolean logic, including: binary operators and if statement."""

from typing import Any
from core.tokens.arthmetic import BinaryOperator

class GreaterThan(BinaryOperator):
    """Implementation of comparison operator *greater than*."""
    def eval(self) -> bool:
        """Determine if the left operand is greater than right operand."""
        return self.left.eval() > self.right.eval()

class LessThan(BinaryOperator):
    """Implementation of comparison operator *less than*."""
    def eval(self) -> bool:
        """Determine if the left operand is smaller than right operand."""
        return self.left.eval() < self.right.eval()

class GreaterOrEqualTo(BinaryOperator):
    """Implementation of comparison operator *greater than or equal to*."""
    def eval(self) -> bool:
        """Determine if the left operand is greater than or equal to the right operand."""
        return self.left.eval() >= self.right.eval()

class LessOrEqualTo(BinaryOperator):
    """Implementation of comparison operator *less than or equal to*."""
    def eval(self) -> bool:
        """Determine if the left operand is smaller than or equal to the right operand."""
        return self.left.eval() <= self.right.eval()

class EqualTo(BinaryOperator):
    """Implementation of comparison operator *equal to*."""
    def eval(self) -> bool:
        """Determine if the left operand is equal to the right operand."""
        return self.left.eval() == self.right.eval()

class IfStatement:
    """Implementation of an `if-then` statement."""
    def __init__(self, condition, instructions) -> None:
        self.condition = condition
        self.instructions = instructions

    def eval(self) -> Any | None:
        """
        Evaluate code inside `if-then` clause under condition that `condition`
        evaluates to `True`.
        """
        if self.condition.eval():
            return self.instructions.eval()
        return None
