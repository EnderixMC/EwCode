"""
Example module for EwCode
(Note: You have to add the Command class to every module)
"""

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
    
class Run(Command):
    arguments = 1
    def get_usage():
        return "run"
    def execute(self):
        eval(self.args[0])

export = [Run]
