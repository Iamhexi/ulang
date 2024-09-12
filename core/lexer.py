"""Module containg µLang lexer."""
from rply import LexerGenerator


class Lexer():
    "Lexer, which recognises pattern in a source code and returns a sequence of tokens."
    def __init__(self):
        self.lexer = LexerGenerator()

    def _add_tokens(self):
        self.lexer.add('string', r'"[^"]*"')
        self.lexer.add('if', r'if')
        self.lexer.add('then', r'then')
        self.lexer.add('var', r'var')
        self.lexer.add('fun', r'fun')
        self.lexer.add('time', r'\d{1,2}:\d{2}')
        self.lexer.add('greater_than', r'>')
        self.lexer.add('greater_or_equal_to', r'>=')
        self.lexer.add('less_than', r'<')
        self.lexer.add('less_or_equal_to', r'<=')
        self.lexer.add('equal_to', r'==')
        self.lexer.add('assign', r'=')
        self.lexer.add('symbol_name', r'[a-zA-Z_][a-zA-Z0-9_\-]*')

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

        self.lexer.ignore(r'\s+')

    def get_lexer(self):
        """
        Supply a µLang-complient lexer.

        Returns
        -------
        Lexer
            An instance of a lexer.
        """
        self._add_tokens()
        return self.lexer.build()
