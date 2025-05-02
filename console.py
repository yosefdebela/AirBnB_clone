#!/usr/bin/python3
"""Module for the entry point of the command interpreter."""

import cmd
from models.base_model import BaseModel
from models import storage
import re
import json
from shlex import split


class HBNBCommand(cmd.Cmd):

    """Class for the command interpreter."""

    prompt = "(hbnb) "

    def default(self, line):
        """Catch commands if nothing else matches then."""
        # print("DEF:::", line)
        self._precmd(line)

    # def _precmd(self, line):
    #     """Intercepts commands to test for class.syntax()"""
    #     # print("PRECMD:::", line)
    #     match = re.search(r"^(\w*)\.(\w+)(?:\(([^)]*)\))$", line)
    #     if not match:
    #         return line
    #     classname = match.group(1)
    #     method = match.group(2)
    #     args = match.group(3)
    #     match_uid_and_args = re.search('^"([^"]*)"(?:, (.*))?$', args)
    #     if match_uid_and_args:
    #         uid = match_uid_and_args.group(1)
    #         attr_or_dict = match_uid_and_args.group(2)
    #     else:
    #         uid = args
    #         attr_or_dict = False
    #
    #     attr_and_value = ""
    #     if method == "update" and attr_or_dict:
    #         match_dict = re.search('^({.*})$', attr_or_dict)
    #         if match_dict:
    #             self.update_dict(classname, uid, match_dict.group(1))
    #             return ""
    #         match_attr_and_value = re.search(
    #             '^(?:"([^"]*)")?(?:, (.*))?$', attr_or_dict)
    #         if match_attr_and_value:
    #             attr_and_value = (match_attr_and_value.group(
    #                 1) or "") + " " + (match_attr_and_value.group(2) or "")
    #     command = method + " " + classname + " " + uid + " " + attr_and_value
    #     self.onecmd(command)
    #     return command

    # def update_dict(self, classname, uid, s_dict):
    #     """Helper method for update() with a dictionary."""
    #     s = s_dict.replace("'", '"')
    #     d = json.loads(s)
    #     if not classname:
    #         print("** class name missing **")
    #     elif classname not in storage.classes():
    #         print("** class doesn't exist **")
    #     elif uid is None:
    #         print("** instance id missing **")
    #     else:
    #         key = "{}.{}".format(classname, uid)
    #         if key not in storage.all():
    #             print("** no instance found **")
    #         else:
    #             attributes = storage.attributes()[classname]
    #             for attribute, value in d.items():
    #                 if attribute in attributes:
    #                     value = attributes[attribute](value)
    #                 setattr(storage.all()[key], attribute, value)
    #             storage.all()[key].save()

    def do_EOF(self, line):
        """Handles End Of File character.
        """
        print()
        return True

    def do_quit(self, line):
        """Exits the program.
        """
        return True

    def emptyline(self):
        """Doesn't do anything on ENTER.
        """
        pass

    def do_create(self, line):
        """Creates an instance.
        """
        word  = line.split(' ')
        if line == "" or line is None:
            print("** class name missing **")
        elif word[0] not in storage.class_dict:
            print("** class doesn't exist **")
        else:
            b = storage.class_dict[word[0]]()
            b.to_dict()
            b.save()
            print(b.id)

    def do_show(self, line):
        """Prints the string representation of an instance.
        """
        if line == "" or line is None:
            print("** class name missing **")
        else:
            words = line.split(' ')
            if words[0] not in storage.class_dict:
                print("** class doesn't exist **")
            elif len(words) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(words[0], words[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[key])

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id.
        """
        if line == "" or line is None:
            print("** class name missing **")
        else:
            words = line.split(' ')
            if words[0] not in storage.class_dict:
                print("** class doesn't exist **")
            elif len(words) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(words[0], words[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    del storage.all()[key]
                    storage.save()

    def do_all(self, line):
        """Prints all string representation of all instances.
        """
        if line != "":
            words = line.split(' ')
            if words[0] not in storage.class_dict:
                print("** class doesn't exist **")
            else:
                nl = [str(obj) for key, obj in storage.all().items()
                      if type(obj).__name__ == words[0]]
                print(nl)
        else:
            new_list = [str(obj) for key, obj in storage.all().items()]
            print(new_list)

    def do_count(self, line):
        """Counts the instances of a class.
        """
        words = line.split(' ')
        if not words[0]:
            print("** class name missing **")
        elif words[0] not in storage.classes():
            print("** class doesn't exist **")
        else:
            matches = [
                k for k in storage.all() if k.startswith(
                    words[0] + '.')]
            print(len(matches))
    def do_print(self, line):
        """Prints the string representation of an instance.
        """
        if line == "" or line is None:
            print("** class name missing **")
        else:
            words = line.split(' ')
            if words[0] not in storage.class_dict:
                print("** class doesn't exist **")
            elif len(words) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(words[0], words[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[key])



    def do_update(self, line):
        """Updates an instance by adding or updating attribute.
        """
        from models import storage
        try:
            if not line:
                raise SyntaxError()
            my_list = split(line, " ")
            if my_list[0] not in storage.class_dict:
                raise NameError()
            if len(my_list) == 1:
                raise IndexError()
            objects = storage.all()
            key = my_list[0] + '.' + my_list[1]
            if key not in objects:
                raise KeyError()
            if len(my_list) < 4:
                raise AttributeError()
            # if len(my_list) < 4:
            #     raise ValueError()
            v = objects[key]
            try:
                v.__dict__[my_list[2]] = eval(my_list[3])
            except Exception:
                v.__dict__[my_list[2]] = my_list[3]
                v.save()
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")
        except IndexError:
            print("** instance id missing **")
        except KeyError:
            print("** no instance found **")
        except AttributeError:
            print("** attribute value missing **")
        except ValueError:
            print("** value missing **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
