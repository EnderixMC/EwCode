from .tokens import *

signs = ["+", "-", "/", "*", "^"]
numTokens = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

class Lexer:
    def lex(self, math):
        self.math = list(math.replace(" ", ""))
        self.tokens = []

        while len(self.math) > 0:
            self.tokens.append(self.nextToken()) 

        return self.tokens

    def lexBrackets(self):
        tokens = []
        while type(token := self.nextToken()) != CloseBracketsToken:
            tokens.append(token)
        return Brackets(tokens)

    def nextToken(self):
        token = self.math.pop(0)
        if token in numTokens:
            number = token
            while len(self.math) > 0 and self.math[0] in numTokens:
                number += self.math.pop(0)
            return NumberToken(float(number))

        elif token in signs:
            return SignToken(token)
        elif token == "(":
            return self.lexBrackets()
        elif token == ")":
            return CloseBracketsToken()

