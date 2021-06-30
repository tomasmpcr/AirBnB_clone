#!/usr/bin/env python3
"""
    that contains the entry point of the command interpreter
"""


from abc import abstractmethod
import cmd
import shlex
from sys import exec_prefix
import models
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

class_list = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
            "Place": Place, "Review": Review, "State": State, "User": User}


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

    #====================================================================================

    def do_create(self, arg):
        if arg == "":
            print("** class name missing **")
            return
        try:
            obj = eval(arg.strip()+"()")
            print(obj.id)
            obj.save()
        except:
            print("** class doesn't exist **")

    def do_show(self, arg):
        args = arg.strip().split(" ")
        if len(args) >= 1 and args[0] == '':
            print("** class name missing **")
            return
        elif args[0] not in class_list.keys():
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return

        bus = args[0] + "." + args[1]
        
        for key, val in models.storage.all().items():
            if bus == key:
                print(val)
                return

    def do_destroy(self, arg):
        args = arg.strip().split(" ")
        if len(args) >= 1 and args[0] == '':
            print("** class name missing **")
            return
        elif args[0] not in class_list.keys():
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return

        bus = args[0] + "." + args[1]
        
        try:
            models.storage.all().pop(bus)
            models.storage.save()
        except:
            print("** no instance found **")

    def do_all(self, arg):
        args = arg.strip().split(" ")
        obj = []
        if len(args) >= 1 and args[0] == '':
            for value in models.storage.all().values():
                obj.append(str(value))
            print("[", end="")
            print(", ".join(obj), end="")
            print("]")
        elif args[0].strip() in class_list:
            for key, val in models.storage.all().items():
                if args[0].strip() in key:
                    obj.append(str(models.storage.all()[key]))
            print("[", end="")
            print(", ".join(obj), end="")
            print("]")
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        args = arg.strip().split(" ")
        if len(args) >= 1 and args[0] == '':
            print("** class name missing **")
            return
        elif args[0] not in class_list.keys():
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return

        bus = args[0] + "." + args[1]
        encontro = False

        for key, val in models.storage.all().items():
            if bus == key:
                encontro = True
                break

        if encontro is False:
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        if len(args) < 4:
            print("** value missing **")
            return

        setattr(val, args[2], args[3])
        models.storage.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
