from ply import yacc
from Lexical_analyzer import LexerAnalyzer


class Parser:
    tokens = LexerAnalyzer().tokens

    def __init__(self):
        # will use in phase 3
        pass

    # functions for each proper rule and creating grammar
    def p_program(self, production_rule):
        # it is non-terminal , so it's like S-> program
        "program : exp"
        print("program : exp")
        """program : declist MAIN LRB RRB block"""
        print("program : declist MAIN LRB RRB block")

    # expression for sum
    def p_expression_sum(self, production_rule):
        "exp : exp SUM exp"
        print("exp : exp SUM exp")

    # expression for sub
    def p_expression_sub(self, production_rule):
        "exp : exp SUB exp"
        print("exp : exp SUB exp")

    # expression for multiplication
    def p_expression_mul(self, production_rule):
        "exp : exp MUL exp"
        print("exp : exp MUL exp")

    # expression for div
    def p_expression_div(self, production_rule):
        "exp : exp DIV exp"
        print("exp : exp DIV exp")

    # expression for integer number
    def p_expression_integer(self, production_rule):
        "exp : INTEGER"
        print("exp : INTEGER")

    def p_error(self, production_rule):
        print(production_rule.value)
        raise Exception('Parsing error : invalid grammar at', production_rule)

    precedence = (
        # 1 + 2 + 3 : we will calculate from left to right
        ('left', 'SUM', 'SUB'),
        ('left', 'MUL', 'DIV')
    )

    # def p_error(self, p):
    #     print(p.value)
    #     raise Exception('ParsingError: invalid grammar at ', p)

    def build(self, **kwargs):
        """build the parser"""
        self.parser = yacc.yacc(module=self, **kwargs)
        return self.parser
