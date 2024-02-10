#!/usr/bin/python
"""
Module for console
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """ Command interpreter for HBNB """
    prompt = "(hbnb) "

    def do_EOF(self, arg):
        """Exit the program"""
        return True

    def help_EOF(self):
        """Display help message for EOF command"""
        print("Exit the program")

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def help_quit(self):
        """Display help message for quit command"""
        print("Quit command to exit the program")

    def emptyline(self):
        """
        Does nothing when an empty line is entered .
        """

    if __name__ == '__main__':
    HBNBCommand().cmdloop()
