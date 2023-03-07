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