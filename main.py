"""
Main module of µLang language implementation. It contains both REPL and code
evaluation function `evaluate()`.
"""
import logging
from typing import Any
import rply
from core.lexer import Lexer
from core.parser import Parser

logger = logging.Logger('Main logger', level=logging.WARNING)

def evaluate(code: str) -> Any:
    """
    Evaluate μLang code.

    Parameters
    ----------
    code : str
        μLang code to be evaluated.

    Returns
    -------
    Any
        Result of the evaluation.
    """
    lexer = Lexer().get_lexer()
    parser_generator = Parser()
    parser_generator.parse()
    parser = parser_generator.get_parser()

    tokens = lexer.lex(code)
    return parser.parse(tokens).eval()  # type: ignore

def repl() -> None:
    """Provide read-eval-print loop (REPL) for μLang."""
    while True:
        try:
            code = input("-> ")
        except KeyboardInterrupt:
            logger.info('Exitting...')
            break

        try:
            print(evaluate(code=code))
        except rply.errors.LexingError as e: # type: ignore
            position = e.source_pos
            logger.critical(
                'Unrecognised thing at line %d, column %d',
                position.lineno,
                position.colno
            )
        except OverflowError as e:
            logger.warning(e.args[1])
        except Exception as e:
            logger.error(e)


if __name__ == '__main__':
    repl()
