"""
EwCode Module: System
"""

from ewcode_lib import Command, variables
import sys

class Exit(Command):
    arguments = 1
    def get_usage():
        return "exit"
    def execute(self):
        sys.exit(self.args[0])

class GetPATH(Command):
    arguments = 1
    def get_usage():
        return "getpath"
    def execute(self):
        variables[self.args[0]] = sys.path

exports = [Exit, GetPATH]