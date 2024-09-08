"""
Module contains arthmetic tokens, mostly arthmetic operands such as plus,
minus *et cetera*.
"""

from core.tokens.literal import Duration

class BinaryOperator():
    """Base class for binary operator, taking left- and righthand operands."""
    def __init__(self, left, right):
        self.left = left
        self.right = right

class Addition(BinaryOperator):
    """Implementation of addition"""
    def eval(self) -> float | Duration:
        """
        Evaluate value of addition.

        Returns
        -------
        float | Time
            `float` for arthmetic addition.
            `Duration` for adding two `Time` instances.
        """
        return self.left.eval() + self.right.eval()

class Subtraction(BinaryOperator):
    """Implementation of a subtraction."""
    def eval(self) -> float | Duration:
        """
        Evaluate value of subtraction.

        Returns
        -------
        float | Duration
            `Difference. float` for numeric operation.
            `Duration` for operation on `Time` instances.
        """
        return self.left.eval() - self.right.eval()

class Multiplication(BinaryOperator):
    """Implementation of multiplication."""
    def eval(self) -> float:
        """
        Evaluate value of multiplication.

        Returns
        -------
        float
            Product.
        """
        return self.left.eval() * self.right.eval()

class Division(BinaryOperator):
    """Implementation of division."""
    def eval(self) -> float:
        """
        Evaluate value of division.

        Returns
        -------
        float
            Quotient.

        Raises
        ------
        ZeroDivisionError
            Raised if division by zero is attempted.
        """
        if self.right.eval() == 0:
            raise ZeroDivisionError("You cannot divide by 0.")
        return self.left.eval() / self.right.eval()

class Exponentiation(BinaryOperator):
    """Implementation of exponentiation."""
    def eval(self) -> float:
        """
        Evaluate value of exponentiation.

        Returns
        -------
        float
            Result of exponentiation.
        """
        return self.left.eval() ** self.right.eval()
