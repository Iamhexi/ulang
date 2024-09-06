from core.tokens.arthmetic import BinaryOperator

class GreaterThan(BinaryOperator):
    def eval(self) -> bool:
        return self.left.eval() > self.right.eval()
    
class LessThan(BinaryOperator):
    def eval(self) -> bool:
        return self.left.eval() < self.right.eval()

class GreaterOrEqualTo(BinaryOperator):
    def eval(self) -> bool:
        return self.left.eval() >= self.right.eval()

class LessOrEqualTo(BinaryOperator):
    def eval(self) -> bool:
        return self.left.eval() <= self.right.eval()

class EqualTo(BinaryOperator):
    def eval(self) -> bool:
        return self.left.eval() == self.right.eval()

class IfStatement:
    def __init__(self, condition, instructions) -> None:
        self.condition = condition
        self.instructions = instructions

    def eval(self) -> any:
        if self.condition.eval():
            return self.instructions.eval()
        return None
