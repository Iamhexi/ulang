"""
Module implementing the µLang parser. Contains production rules for the language.
"""

from types import NoneType
from typing import Any
from rply import ParserGenerator

from core.tokens.arthmetic import (
    Addition,
    BinaryOperator,
    Division,
    Exponentiation,
    Multiplication,
    Subtraction,
)
from core.tokens.logic import (
    EqualTo,
    GreaterOrEqualTo,
    GreaterThan,
    IfStatement,
    LessOrEqualTo,
    LessThan,
)
from core.tokens.literal import Duration, Number, String, Time


class Parser:
    """µLang Parser with production rules encoded."""
    def __init__(self):
        self.pg = ParserGenerator(
            tokens=[
                "time",
                "number",
                "exponentiation",
                "division",
                "multiplication",
                "addition",
                "subtraction",
                "string",
                "if",
                "then",
                "greater_than",
                "greater_or_equal_to",
                "less_than",
                "less_or_equal_to",
                "equal_to",
            ],

            precedence=[
                ('left', ['addition', 'subtraction']),
                ('left', ['multiplication', 'division']),
                ('left', ['exponentiation']),
            ],
        )

    def parse(self):
        """
        Parse tokens, build AST with production rules.

        Returns
        -------
        _type_
            _description_

        Raises
        ------
        TypeError
            _description_
        TypeError
            _description_
        ValueError
            _description_
        """
        @self.pg.production("program : expression ")
        def program(p) -> Any:
            return p[0]

        @self.pg.production("expression : if boolean_expression then expression")
        def condition(p):
            return IfStatement(p[1], p[3])

        @self.pg.production(
            "arthmetic_expression : arthmetic_expression subtraction arthmetic_expression"
        )
        @self.pg.production(
            "arthmetic_expression : arthmetic_expression addition arthmetic_expression"
            )
        @self.pg.production(
            "arthmetic_expression : arthmetic_expression multiplication arthmetic_expression"
        )
        @self.pg.production(
            "arthmetic_expression : arthmetic_expression division arthmetic_expression"
            )
        @self.pg.production(
            "arthmetic_expression : arthmetic_expression exponentiation arthmetic_expression"
        )
        def addition_expression(p) -> BinaryOperator:
            operator = p[1].gettokentype()
            match operator:
                case "multiplication":
                    return Multiplication(p[0], p[2])
                case "addition":
                    return Addition(p[0], p[2])
                case "subtraction":
                    return Subtraction(p[0], p[2])
                case "division":
                    return Division(p[0], p[2])
                case "exponentiation":
                    return Exponentiation(p[0], p[2])
                case _:
                    raise TypeError(f"Unknown operator: {operator}")

        @self.pg.production(
            "boolean_expression : arthmetic_expression equal_to arthmetic_expression"
        )
        @self.pg.production(
            "boolean_expression : arthmetic_expression less_than arthmetic_expression"
        )
        @self.pg.production(
            "boolean_expression : arthmetic_expression less_or_equal_to arthmetic_expression"
        )
        @self.pg.production(
            "boolean_expression : arthmetic_expression greater_or_equal_to arthmetic_expression"
        )
        @self.pg.production(
            "boolean_expression : arthmetic_expression greater_than arthmetic_expression"
        )
        def boolean_expression(p):
            evaluation_type: type = NoneType
            operator = p[1].gettokentype()
            match operator:
                case "equal_to":
                    evaluation_type = EqualTo
                case "less_than":
                    evaluation_type = LessThan
                case "less_or_equal_to":
                    evaluation_type = LessOrEqualTo
                case "greater_or_equal_to":
                    evaluation_type = GreaterOrEqualTo
                case "greater_than":
                    evaluation_type = GreaterThan
                case _:
                    raise TypeError(
                        f"Unkown operator for boolean expression: {operator}"
                    )

            left_operand = p[0]
            right_operand = p[2]
            return evaluation_type(left_operand, right_operand)

        @self.pg.production('expression : duration')
        def duration(p):
            return Duration(p[0])

        @self.pg.production('expression : time')
        def time_to_expression(p):
            return Time(p[0].value)

        @self.pg.production('duration : time subtraction time')
        def time_subtraction(p):
            time1 = Time(p[0].value)
            time2 = Time(p[2].value)
            return time1 - time2

        @self.pg.production("expression : arthmetic_expression")
        def expression_from_arthmetic_expression(p):
            return p[0]

        @self.pg.production("expression : boolean_expression")
        def expression_from_boolean_expression(p):
            return p[0]

        @self.pg.production("arthmetic_expression : number")
        def number(p):
            return Number(p[0].value)

        @self.pg.production("expression : string")
        def string(p):
            return String(p[0].value)

        @self.pg.error
        def error_handle(token):
            raise ValueError(token)

    def get_parser(self):
        """
        Supply an instance of a parser, using µLang production rules and
        tokens.

        Returns
        -------
        LRParser
            An instance of a parser.
        """
        return self.pg.build()
