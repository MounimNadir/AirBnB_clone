#!/usr/bin/python
"""
Module for console
"""
import cmd
import re
import shlex
import ast
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State
from models.city import City


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    valid_classes = ["BaseModel", "User", "Amenity",
                     "Place", "Review", "State", "City"]

    def emptyline(self):
        """
        Does nothing when an empty line is entered .
        """
    def help_quit(self):
        
        """Display help message for quit command"""
        print("Quit command to exit the program")

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program"""
        return True
    def do_create(self, arg):
        """Create a new instance of a specified class."""
        commands = shlex.split(arg)
        
        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in self.valid_classes:
            print("** class doesn't exist **")
        else:
            new_instance = eval(f"{commands[0]}()")
            storage.save()
            print(new_instance.id)

    def do_show(self, arg):
        """Show the string representation of an instance based on the class name and id."""
        commands = shlex.split(arg)
        
        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(commands) == 1:
            print("** instance id missing **")
        else:
            key = commands[0] + "." + commands[1]
            if key not in storage.all():
                print("** no instance found **")
            else:
                print(storage.all()[key])

    def do_destroy(self, arg):
        """Delete an instance based on the class name and id."""
        commands = shlex.split(arg)
        
        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(commands) == 1:
            print("** instance id missing **")
        else:
            key = commands[0] + "." + commands[1]
            if key not in storage.all():
                print("** no instance found **")
            else:
                del storage.all()[key]
                storage.save()

    def do_all(self, arg):
        """Print all string representation of all instances based or not on the class name."""
        objects = storage.all()
        
        commands =shlex.split(arg)
        
        if len(commands) == 0:
            for key, value in objects.items():
                print(str(value))
        elif commands[0] not in self.valid_classes:
            print("** class doesn't exist **")
        else:
            for key, value in objects.items():
                if key.split('.')[0] == commands[0]:
                    print(str(value))
def do_update(self, arg):
    """Update an instance based on the class name and id by adding or updating attribute."""
    commands = shlex.split(arg)

    if len(commands) == 0:
        print("** class name missing **")
    elif commands[0] not in self.valid_classes:
        print("** class doesn't exist **")
    elif len(commands) == 1:
        print("** instance id missing **")
    elif len(commands) == 2:
        print("** attribute name missing **")
    elif len(commands) == 3:
        print("** value missing **")
    else:
        key = commands[0] + "." + commands[1]
        if key not in storage.all():
            print("** no instance found **")
        else:
            instance = storage.all()[key]
            attr = commands[2]
            value = commands[3]
            setattr(instance, attr, value)
            storage.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()