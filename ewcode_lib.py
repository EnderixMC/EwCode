from time import sleep

delay = 0.01
def Execute(code):
    for i in code:
        sleep(delay)
        function = i[0][1]
        i.pop(0)
        args = []
        for arg in i:
            if arg[0] == "VAR":
                args.append(variables[arg[1]])
            else:
                args.append(arg[1])
        for command in commands:
            if function == command.get_usage():
                command(args).execute()

class Command:
    arguments = 0
    def __init__(self, args):
        if self.arguments == len(args) or self.arguments == -1:
            self.args = args
        else:
            raise InvalidArgumentException()
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

class InvalidArgumentException (Exception):
    pass

commands = [Print,Set,Input]
variables = {}
