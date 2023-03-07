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

class Operation:
    def __init__(self):
        pass

class NumberOperation(Operation):
    def __init__(self, number):
        self.number = number

    def execute(self):
        return self.number

class SignOperation(Operation):
    def __init__(self, lhs, rhs):
        self.lhs = lhs
        self.rhs = rhs

    def execute(self):
        return self.calculate(self.lhs.execute(), self.rhs.execute())

    def calculate(self, lhs, rhs):
        pass

class PlusOperation(SignOperation):
    def calculate(self, lhs, rhs):
        return lhs + rhs

class SubtractOperation(SignOperation):
    def calculate(self, lhs, rhs):
        return lhs - rhs

class MultiplyOperation(SignOperation):
    def calculate(self, lhs, rhs):
        return lhs * rhs

class DivideOperation(SignOperation):
    def calculate(self, lhs, rhs):
        return lhs / rhs

class ExponentOperation(SignOperation):
    def calculate(self, lhs, rhs):
        return lhs ** rhs