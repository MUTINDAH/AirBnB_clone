#!/usr/bin/python3
import cmd


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print()
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass

    def help_quit(self):
        """Display help message for quit command"""
        print("Quit the program")

    def help_EOF(self):
        """Display help message for EOF command"""
        print("Exit the program")

    def help_help(self):
        """Display help message for help command"""
        print("Display available commands")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
