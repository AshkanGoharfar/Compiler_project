from Lexical_analyzer import LexerAnalyzer
from Parser import Parser

# lexer analyzer test
lexerAnalyzer = LexerAnalyzer()
lexer_builder = lexerAnalyzer.build()
input = open("my_test.txt")
text_input = input.read()
input.close()
output = open("my_output.txt", "w")
lexer_builder.input(text_input)

# parser test
parser = Parser()
parser.build().parse(text_input, lexer_builder, False)

# while True:
#     tokens = lexer_builder.token()
#     if not tokens:
#         break
#     output.write(str(tokens) + '\n')
# output.close()

