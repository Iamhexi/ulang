from rply import ParserGenerator

from core.ast import Addition, Division, Exponentiation, Multiplication, Number, String, Subtraction, Time

class Parser():
    def __init__(self):
        self.pg = ParserGenerator([
            'time',
            'number',
            # 'opening_parenthesis',
            # 'closing_parenthesis',
            'exponentiation',
            'division',
            'multiplication',
            'addition',
            'subtraction',
            'string',
        ])

    def parse(self):
        @self.pg.production('program : expression ')
        def program(p):
            return p[0]

        @self.pg.production('expression : expression addition term')
        def addition_expression(p):
            return Addition(p[0], p[2])

        @self.pg.production('expression : expression subtraction term')
        def subtraction_expression(p):
            return Subtraction(p[0], p[2])
        
        @self.pg.production('expression : expression multiplication term')
        def multiplication_expression(p):
            return Multiplication(p[0], p[2])
        
        @self.pg.production('expression : expression division term')
        def division_expression(p):
            return Division(p[0], p[2])
        
        @self.pg.production('expression : expression exponentiation term')
        def exponentiation_expression(p):
            return Exponentiation(p[0], p[2])

        @self.pg.production('expression : term')
        def term(p):
            return p[0]

        @self.pg.production('term : number')
        def number(p):
            return Number(p[0].value)
        
        @self.pg.production('term : string')
        def string(p):
            return String(p[0].value)
        
        @self.pg.production('term : time')
        def time(p):
            return Time(p[0].value)

        @self.pg.error
        def error_handle(token):
            raise ValueError(token)

    def get_parser(self):
        return self.pg.build()
