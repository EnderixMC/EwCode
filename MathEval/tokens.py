class Token:
    pass

class OpenBracketsToken(Token):
    pass

class CloseBracketsToken(Token):
    pass

class Brackets(Token):
    def __init__(self, tokens):
        self.tokens = tokens
        
    def __repr__(self):
        return f"<Brackets tokens={self.tokens}>"

class SignToken(Token):
    def __init__(self, sign):
        self.sign = sign
        
    def __repr__(self):
        return f"<SignToken value={self.sign}>"

class NumberToken(Token):
    def __init__(self, number):
        self.number = number
    
    def __repr__(self):
        return f"<NumberToken value={self.number}>"