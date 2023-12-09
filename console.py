#!/usr/bin/python3
"""HBNB Command"""
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """Cmd"""
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    do_EOF = do_quit

    def do_help(self, arg):
        """Ask for help"""
        cmd.Cmd.do_help(self, arg)

    def emptyline(self):
        """Just empty"""
        pass

    def do_create(self, arg):
        """Create a new instance of BaseModel, save it, and print the id"""
        if not arg:
            print("** class name missing **")
            return
        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        try:
            if args[0] not in storage.classes():
                print("** class doesn't exist **")
                return
            if len(args) < 2:
                print("** instance id missing **")
                return
            obj_key = "{}.{}".format(args[0], args[1])
            if obj_key not in storage.all():
                print("** no instance found **")
                return
            print(storage.all()[obj_key])
        except:
            pass

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        try:
            if args[0] not in storage.classes():
                print("** class doesn't exist **")
                return
            if len(args) < 2:
                print("** instance id missing **")
                return
            obj_key = "{}.{}".format(args[0], args[1])
            if obj_key not in storage.all():
                print("** no instance found **")
                return
            del storage.all()[obj_key]
            storage.save()
        except:
            pass

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        args = arg.split()
        try:
            if args and args[0] not in storage.classes():
                print("** class doesn't exist **")
                return
            result = [str(value) for key, value in storage.all().items()]
            print(result)
        except:
            pass

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = arg.split()
        try:
            if not args:
                print("** class name missing **")
                return
            if args[0] not in storage.classes():
                print("** class doesn't exist **")
                return
            if len(args) < 2:
                print("** instance id missing **")
                return
            obj_key = "{}.{}".format(args[0], args[1])
            if obj_key not in storage.all():
                print("** no instance found **")
                return
            if len(args) < 3:
                print("** attribute name missing **")
                return
            if len(args) < 4:
                print("** value missing **")
                return
            obj_instance = storage.all()[obj_key]
            attr_name = args[2]
            attr_value = args[3]
            try:
                attr_value = eval(attr_value)
            except:
                pass
            setattr(obj_instance, attr_name, attr_value)
            storage.save()
        except:
            pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
