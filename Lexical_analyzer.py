from Reserved import *
from ply import lex


class LexerAnalyzer:
    # Lexeme
    t_ASSIGN = r'\='
    t_SUM = r'\+'
    t_SUB = r'\-'
    t_MUL = r'\*'
    t_DIV = r'\/'
    t_MOD = r'\%'
    t_GT = r'\>'
    t_GE = r'\>='
    t_LT = r'\<'
    t_LE = r'\<='
    t_EQ = r'\=='
    t_NE = r'\!='
    t_LCB = r'\{'
    t_RCB = r'\}'
    t_LRB = r'\('
    t_RRB = r'\)'
    t_LSB = r'\['
    t_RSB = r'\]'
    t_SEMICOLON = r';'
    t_COLON = r':'
    t_COMMA = r','
    t_ignore = '\n \t\r\f\v'

    # Tokens
    tokens = [
        'ID', 'INTEGERNUMBER', 'FLOATNUMBER', 'INTEGER', 'FLOAT', 'BOOLEAN', 'FUNCTION',
        'TRUE', 'FALSE', 'PRINT', 'RETURN', 'MAIN', 'IF', 'ELSE', 'ELSEIF', 'WHILE', 'ON',
        'WHERE', 'FOR', 'AND', 'OR', 'NOT', 'IN', 'ASSIGN', 'SUM', 'SUB', 'MUL', 'DIV',
        'MOD', 'GT', 'GE', 'LT', 'LE', 'EQ', 'NE', 'LCB', 'RCB', 'LRB', 'RRB', 'LSB', 'RSB',
        'SEMICOLON', 'COLON', 'COMMA', 'ERROR', 'VOID'
    ]

    # Check for correct IDs

    def t_ID(self, t):
        r'[a-z_]([a-zA-Z0-9_])*'
        if t.value in reserved:
            t.type = reserved[t.value]
        return t

    # Check is True or not
    def t_TRUE(self, t):
        r'True'
        return t

    # Check is False or not
    def t_FALSE(self, t):
        r'False'
        return t

    # ERROR
    def t_ERROR(self, t):
        r"""([0-9A-Z]([0-9]*[a-zA-Z_][0-9]*)+)
        | ([A-Z][0-9a-zA-Z_]*)
        | (\.[0-9]+)
        | (([0-9]+\.[0-9]+\.)[0-9\.]*)
        | (0*((?=[0-9]{11,}\.)(([1-9]+0*)+|0)\.((0*[1-9]+)+|0))0*)
        | (0*[1-9][0-9]{10,})
        | ([/%\-\*\+]\s*([/%\-\*\+]\s*)+)
        """
        return t

    # Check is float or not
    def t_FLOATNUMBER(self, t):
        r'0*((([1-9]+0*)+|0)\.((0*[1-9]+)+|0))0*'
        t.value = float(t.value)
        return t

    # Check is integer or not
    def t_INTEGERNUMBER(self, t):
        r"""[0-9]+"""
        p = int(t.value)
        t.value = int(t.value)
        if p > 999999999:
            t.type = 'ERROR'
            return t
        else:
            return t

    # go to next line
    def t_newline(self, t):
        r"""\n+"""
        t.lexer.lineno += len(t.value)

    def t_error(self, t):
        raise Exception('Error at ', t.value[0])

    def build(self, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)
        return self.lexer
