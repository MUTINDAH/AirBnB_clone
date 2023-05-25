#!/usr/bin/python3
"""
A module that implements the HBNBCommand class
"""
import cmd
import models


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    class_names = ["BaseModel"]

    def do_create(self, arg):
        """Creates a new instance of BaseModel"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.class_names:
            print("** class doesn't exist **")
            return
        instance = eval(f"models.{class_name}()")
        instance.save()
        print(instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.class_names:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = class_name + "." + instance_id
        objects = models.storage.all()
        if key in objects:
            print(objects[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.class_names:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = class_name + "." + instance_id
        objects = models.storage.all()
        if key in objects:
            del objects[key]
            models.storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representations of instances"""
        objects = models.storage.all()
        if not arg:
            print([str(obj) for obj in objects.values()])
        else:
            args = arg.split()
            class_name = args[0]
            if class_name not in self.class_names:
                print("** class doesn't exist **")
                return
            filtered = [str(obj) for obj in objects.values()
                        if obj.__class__.__name__ == class_name]
            print(filtered)

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.class_names:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = class_name + "." + instance_id
        objects = models.storage.all()
        if key not in objects:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        attribute_name = args[2]
        if len(args) < 4:
            print("** value missing **")
            return
        value = args[3]
        instance = objects[key]
        setattr(instance, attribute_name, value)
        instance.save()

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print()
        return True

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
