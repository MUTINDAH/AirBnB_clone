#!/usr/bin/python3
""" Command interpreter console """

import cmd


class HBNBCommand(cmd.Cmd):
    """Entry point of the command interpreter"""
    prompt = "(hbnb) "

    def emptyline(self):
        """ Ignore empty spaces """
        pass

    def do_quit(self, arg):
        """ Quit command to exit the program """
        return True

    def do_EOF(self, arg):
        """ Exit the program """
        print()
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
