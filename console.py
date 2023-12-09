#!/usr/bin/python3
"""HBNB Command"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Cmd"""
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """quit"""
        return True

    do_EOF = do_quit

    def do_help(self, arg):
        """Ask for help"""
        cmd.Cmd.do_help(self, arg)

    def emptyline(self):
        """Just empty"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
