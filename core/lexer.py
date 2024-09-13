"""Module containg µLang lexer."""
from rply import lexer, LexerGenerator


class Lexer(): # pylint: disable=too-few-public-methods
    "Lexer, which recognises pattern in a source code and returns a sequence of tokens."
    def __init__(self) -> None:
        self._lexer = LexerGenerator()

    def _add_tokens(self) -> None:
        self._lexer.add('string', r'"[^"]*"')
        self._lexer.add('if', r'if')
        self._lexer.add('then', r'then')
        self._lexer.add('var', r'var')
        self._lexer.add('fun', r'fun')
        self._lexer.add('time', r'\d{1,2}:\d{2}')
        self._lexer.add('greater_than', r'>')
        self._lexer.add('greater_or_equal_to', r'>=')
        self._lexer.add('less_than', r'<')
        self._lexer.add('less_or_equal_to', r'<=')
        self._lexer.add('equal_to', r'==')
        self._lexer.add('assign', r'=')
        self._lexer.add('symbol_name', r'[a-zA-Z_][a-zA-Z0-9_\-]*')

        float_pattern = r'((?<![\w.])[+-]?(?:\d+\.\d+|\d+\.|\.\d+|\d+)(?:[eE][+-]?\d+)?(?![\w.]))'
        integer_pattern = r'[+-]?\d+'
        self._lexer.add('number', fr'{float_pattern}|{integer_pattern}')

        # self.lexer.add('print', r'print')
        self._lexer.add('opening_parenthesis', r'\(')
        self._lexer.add('closing_parenthesis', r'\)')
        # self.lexer.add('semicolon', r'\;')

        self._lexer.add('addition', r'\+')
        self._lexer.add('subtraction', r'\-')
        self._lexer.add('multiplication', r'\*')
        self._lexer.add('division', r'\/')
        self._lexer.add('exponentiation', r'\^')

        self._lexer.ignore(r'\s+')

    def get_lexer(self) -> lexer.Lexer:
        """
        Supply a µLang-complient lexer.

        Returns
        -------
        Lexer
            An instance of a lexer.
        """
        self._add_tokens()
        return self._lexer.build()
