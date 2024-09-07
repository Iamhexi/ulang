import logging
import rply
from core.lexer import Lexer
from core.parser import Parser

logger = logging.Logger('Main logger', level=logging.WARNING)

def evaluate(code: str) -> any:
    """
    Evaluate μLang code.

    Parameters
    ----------
    code : str
        μLang code to be evaluated.

    Returns
    -------
    any
        Result of the evaluation.
    """
    lexer = Lexer().get_lexer()
    parser_generator = Parser()
    parser_generator.parse()
    parser = parser_generator.get_parser()

    tokens = lexer.lex(code)
    return parser.parse(tokens).eval()

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
        except rply.errors.LexingError as e:
            position = e.source_pos
            logger.critical(
                'Unrecognised thing at line %d, column %d',
                position.lineno,
                position.colno
            )
        except Exception as e:
            logger.error(e)


if __name__ == '__main__':
    repl()
