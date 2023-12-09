#!/usr/bin/python3
"""HBNB Command"""
import cmd


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """"""
        return True

    def do_help(self, arg):
        """"""
        cmd.Cmd.do_help(self, arg)

    def do_create(self, arg):
        """"""

    def emptyline(self):
        """Just empty"""
        pass

    def do_show(self, arg):
        """"""
        pass
