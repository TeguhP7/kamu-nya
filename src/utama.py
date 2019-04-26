import lexer
import urai_pharser

def main():
    content = ""
    with open('tes.tp', 'r') as file:
        content = file.read()

    #Lexer
    lex = lexer.Lexer(content)

    tokens = lex.tokenize()

    #Parser
    diuraikan_parse = urai_pharser.penguraian_parser(tokens)
    objs  = diuraikan_parse.diuraikan_parse()

main()