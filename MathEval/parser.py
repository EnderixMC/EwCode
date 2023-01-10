from .tokens import *
from .operations import *

tokenPirority = {
    "+": 1,
    "-": 1,
    "*": 2,
    "/": 2,
    "^": 3
}

def signOperationFromToken(token, lhs, rhs):
    if token.sign == "+":
        return PlusOperation(lhs, rhs)
    elif token.sign == "-":
        return SubtractOperation(lhs, rhs)
    elif token.sign == "*":
        return MultiplyOperation(lhs, rhs)
    elif token.sign == "/":
        return DivideOperation(lhs, rhs)
    elif token.sign == "^":
        return ExponentOperation(lhs, rhs)

def parse(tokens):
    if len(tokens) == 1:
        if type(tokens[0]) == NumberToken:
            return NumberOperation(tokens[0].number)
        elif type(tokens[0]) == Brackets:
            return parse(tokens[0].tokens)
    else:
        index = 0
        pirority = 10
        for i in range(len(tokens) - 1, -1, -1):
            if type(tokens[i]) == SignToken:
                if tokenPirority[tokens[i].sign] < pirority:
                    index = i
                    pirority = tokenPirority[tokens[i].sign]
        return signOperationFromToken(tokens[index], parse(tokens[:index]), parse(tokens[index+1:]))
        
