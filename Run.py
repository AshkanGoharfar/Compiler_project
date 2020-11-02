from Lexical_analyzer import LexerAnalyzer

lexerAnalyzer = LexerAnalyzer()
lexer_builder = lexerAnalyzer.build()
input = open("test3.txt")
text_input = input.read()
input.close()
output = open("output1.txt", "w")
lexer_builder.input(text_input)
while True:
    tokens = lexer_builder.token()
    if not tokens:
        break
    output.write(str(tokens) + '\n')
output.close()
