"""
Example module for EwCode
"""

from ewcode_lib import Command

class Run(Command):
    arguments = 1
    def get_usage():
        return "run"
    def execute(self):
        eval(self.args[0])

exports = [Run]
