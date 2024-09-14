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

def evaluate(
    code: str,
    lexer: Lexer | None = None,
    parser: Parser | None = None,
) -> Any:
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
    if lexer is None:
        lexer = Lexer().get_lexer()
    if parser is None:
        parser_generator = Parser()
        parser_generator.parse()
        parser = parser_generator.get_parser()

    tokens = lexer.lex(code)
    return parser.parse(tokens) # type: ignore


def repl() -> None:
    """Provide read-eval-print loop (REPL) for μLang."""
    lexer = Lexer().get_lexer()

    parser_generator = Parser()
    parser_generator.parse()
    parser = parser_generator.get_parser()

    while True:
        try:
            code = input("-> ")
        except KeyboardInterrupt:
            logger.info('Exitting...')
            break

        try:
            print(evaluate(code=code, lexer=lexer, parser=parser))
        except rply.errors.LexingError as e: # type: ignore
            position = e.source_pos
            logger.critical(
                'Unrecognised thing at line %d, column %d',
                position.lineno,
                position.colno
            )
        except OverflowError as e:
            logger.warning(e.args[1])
        except Exception as e: # pylint: disable=broad-exception-caught
            logger.error(e)


if __name__ == '__main__':
    repl()
