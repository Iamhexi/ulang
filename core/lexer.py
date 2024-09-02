from rply import LexerGenerator


class Lexer():
    def __init__(self):
        self.lexer = LexerGenerator()

    def _add_tokens(self):
        self.lexer.add('time', r'\d{1,2}:\d{2}')

        float_pattern = r'((?<![\w.])[+-]?(?:\d+\.\d+|\d+\.|\.\d+|\d+)(?:[eE][+-]?\d+)?(?![\w.]))'
        integer_pattern = r'[+-]?\d+'
        self.lexer.add('number', fr'{float_pattern}|{integer_pattern}')

        # self.lexer.add('print', r'print')
        self.lexer.add('opening_parenthesis', r'\(')
        self.lexer.add('closing_parenthesis', r'\)')
        # self.lexer.add('semicolon', r'\;')

        self.lexer.add('addition', r'\+')
        self.lexer.add('subtraction', r'\-')
        self.lexer.add('multiplication', r'\*')
        self.lexer.add('division', r'\/')
        self.lexer.add('exponentiation', r'\^')

        self.lexer.add('string', r'"[^"]*"')
        self.lexer.ignore(r'\s+')

    def get_lexer(self):
        self._add_tokens()
        return self.lexer.build()