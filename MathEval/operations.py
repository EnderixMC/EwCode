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