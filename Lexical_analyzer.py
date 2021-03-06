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
        'ID', 'INTEGER', 'FLOAT', 'BOOLEAN', 'FUNCTION',
        'TRUE', 'FALSE', 'PRINT', 'RETURN', 'MAIN', 'IF', 'ELSE', 'ELSEIF', 'WHILE', 'ON',
        'WHERE', 'FOR', 'AND', 'OR', 'NOT', 'IN', 'ASSIGN', 'SUM', 'SUB', 'MUL', 'DIV',
        'MOD', 'GT', 'GE', 'LT', 'LE', 'EQ', 'NE', 'LCB', 'RCB', 'LRB', 'RRB', 'LSB', 'RSB',
        'SEMICOLON', 'COLON', 'COMMA', 'ERROR'
    ]

    def t_ID(self, t):
        r"""[a-zA-Z\x80-\xff_][a-zA-Z0-9\x80-\xff_]*"""
        if t.value in reserved:
            t.type = reserved[t.value]
        return t

    def t_TRUE(self, t):
        r'True'
        return t

    def t_FALSE(self, t):
        r'False'
        return t

    def t_ERROR(self, t):
        r"""([0-9]+[a-zA-Z_]+)
            |([A-Z]+[0-9a-zA-Z_]+)
            |([\*\+\-\%\/][\s]*[\*\+\-\%\/][\*\+\-\%\/ ]*)
            |([\w\d]*(\.[\w\d]*){2,})
            """
        t.type = 'ERROR'
        return t

    def t_FLOAT(self, t):
        r"""\d+\.\d+"""
        before, after = str(t.value).split('.')
        if len(before) >= 10:
            t.type = 'ERROR'
            return t
        else:
            t.value = float(t.value)
            return t

    def t_INTEGER(self, t):
        r"""[0-9]+"""
        p = int(t.value)
        t.value = int(t.value)
        if p > 999999999:
            t.type = 'ERROR'
            return t
        else:
            return t

    def t_newline(self, t):
        r"""\n+"""
        t.lexer.lineno += len(t.value)

    def t_error(self, t):
        raise Exception('Error at ', t.value[0])

    def build(self, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)
        return self.lexer

    # if there is shoft reduce in grammar it means our grammar is ambigiuose
    # else if there is reduce reduce it means our grammar has error
