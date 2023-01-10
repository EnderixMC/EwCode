from .lexer import Lexer
from .parser import parse

def calculate(math):
    lex = Lexer()
    tokens = lex.lex(math)
    syntaxTree = parse(tokens)
    return syntaxTree.execute()
