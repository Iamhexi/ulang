"""
Module contains arthmetic tokens, mostly arthmetic operands such as plus,
minus *et cetera*.
"""


from core.tokens.literal import Time

class BinaryOperator():
    def __init__(self, left, right):
        self.left = left
        self.right = right

class Addition(BinaryOperator):
    def eval(self) -> float | Time:
        return self.left.eval() + self.right.eval()

class Subtraction(BinaryOperator):
    def eval(self) -> float:
        return self.left.eval() - self.right.eval()

class Multiplication(BinaryOperator):
    def eval(self) -> float:
        return self.left.eval() * self.right.eval()
    
class Division(BinaryOperator):
    def eval(self) -> float:
        if self.right.eval() == 0:
            raise ZeroDivisionError("You cannot divide by 0.")
        return self.left.eval() / self.right.eval()

class Exponentiation(BinaryOperator):
    def eval(self) -> float:
        return self.left.eval() ** self.right.eval()

