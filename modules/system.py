"""
EwCode Module: System
"""

from ewcode_lib import Command
import sys

class Exit(Command):
    arguments = 1
    def get_usage():
        return "exit"
    def execute(self):
        sys.exit(self.args[0])

exports = [Exit]