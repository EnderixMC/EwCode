from MathEval import calculate
from random import randint
from copy import deepcopy
from time import sleep
import sys
import os
import re

commands = []

delay = 0.01
def Execute(code_tmp):
    code = list(code_tmp)
    for i in code:
        sleep(delay)
        if i[0][0] == "CUSTOM_FUNC":
            functions[i[0][1][0]] = i[0][1][1]
            continue
        function = i[0][1]
        i.pop(0)
        args = []
        arg_types = []
        for arg in i:
            if arg[0] == "VAR":
                args.append(variables[arg[1]])
            elif arg[0] == "EQU":
                results = re.findall("{\w+}", arg[1])
                for result in results:
                    arg = (arg[0],arg[1].replace(result, str(variables[result[1:len(result)-1]])))
                try:
                    ans = calculate(arg[1])
                    args.append(int(ans))
                except IndexError as e:
                    raise SyntaxError("Not a valid equation!")
            elif arg[0] == "BOOL" and not (function == "loop" or function == "looprange"):
                args.append(ProcessBool(arg[1]))
            else:
                args.append(arg[1])
        for command in commands:
            if function == command.get_usage():
                #print(command.get_usage(), args)
                command(args).execute()

def ProcessBool(statement):
    results = re.findall("{\w+}", statement)
    for result in results:
        statement = statement.replace(result, str(variables[result[1:len(result)-1]]))
    try:
        ans = eval(re.search("^(?:(True|False)|(True|False)(==|!=)(True|False)|\d+(==|!=|<|>|<=|>=)\d+)$", statement)[0])
        return ans
    except TypeError as e:
        raise SyntaxError("Not a valid statement!")

class Command:
    arguments = 0
    def __init__(self, args):
        if self.arguments == len(args) or self.arguments == -1:
            self.args = args
        else:
            raise InvalidArgumentException(f"{self.arguments} : {len(args)}")
    def get_usage():
        return None
    def execute(self):
        return None

class Print(Command):
    arguments = -1
    def get_usage():
        return "print"
    def execute(self):
        for i in self.args:
            print(i, end="")
        print()

class Set(Command):
    arguments = 2
    def get_usage():
        return "set"
    def execute(self):
        variables[self.args[0]] = self.args[1]

class Input(Command):
    arguments = 2
    def get_usage():
        return "input"
    def execute(self):
        variables[self.args[0]] = input(self.args[1])

class Random(Command):
    arguments = 3
    def get_usage():
        return "random"
    def execute(self):
        variables[self.args[0]] = randint(self.args[1],self.args[2])

class If(Command):
    arguments = 2
    def get_usage():
        return "if"
    def execute(self):
        if self.args[0]:
            Execute(deepcopy(self.args[1]))

class LoopRange(Command):
    arguments = 2
    def get_usage():
        return "looprange"
    def execute(self):
        for i in range(self.args[0]):
            Execute(deepcopy(self.args[1]))

class Loop(Command):
    arguments = 2
    def get_usage():
        return "loop"
    def execute(self):
        while ProcessBool(deepcopy(self.args[0])):
            Execute(deepcopy(self.args[1]))

class Call(Command):
    arguments = 1
    def get_usage():
        return "call"
    def execute(self):
        Execute(deepcopy(functions[self.args[0]]))

class Import(Command):
    arguments = 1
    def get_usage():
        return "import"
    def execute(self):
        global commands
        filepath = sys.argv[1].split("\\")
        path = filepath[len(filepath)-2]
        sys.path.append(os.path.abspath(path))
        commands = commands+__import__(self.args[0]).export

class InvalidArgumentException (Exception):
    pass

commands = commands+[Print,Set,Input,Random,If,Loop,LoopRange,Call,Import]
functions = {}
variables = {}
