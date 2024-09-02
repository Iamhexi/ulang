import logging
import rply
from core.lexer import Lexer
from core.parser import Parser

if __name__ == '__main__':
    logger = logging.Logger('Main logger', level=logging.WARNING)
    
    lexer = Lexer().get_lexer()
    parser_generator = Parser()
    parser_generator.parse()
    parser = parser_generator.get_parser()

    while True:
        code = input("-> ")
        tokens = lexer.lex(code)
        try:
            print( parser.parse(tokens).eval() )
        except rply.errors.LexingError as e:
            position = e.source_pos
            logger.critical(f'Unrecognised thing at line {position.lineno}, column {position.colno}')
        except Exception as e:
            logger.error(e)

