#!/usr/bin/env python3
"""
    that contains the entry point of the command interpreter
"""


import cmd
import shlex
import models


class HBNBCommand(cmd.Cmd):
    """Simple command processor example."""
    prompt = '(hbnb) '

    def do_EOF(self, line):
        """Quit command to exit the program\n"""
        return True

    def do_help(self, arg):
        """help is a help"""
        return super().do_help(arg)

    def do_quit(self, arg):
        """Quit command to exit the program\n"""
        return True

    def emptyline(self):
        """blank line"""
        return False

if __name__ == '__main__':
    HBNBCommand().cmdloop()
