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
        
