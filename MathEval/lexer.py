"""
    EwCode - The most disgusting programming language (https://github.com/EnderixMC/EwCode)
    Copyright (C) 2022-2023  EnderixMC

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as published
    by the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

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

