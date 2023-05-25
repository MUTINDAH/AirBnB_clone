#!/usr/bin/python3

from datetime import datetime
from uuid import uuid4

import json


class FileStorage:
    """File storage class for all other classes."""

    __file_path: str = "file.json"
    __objects: dict = {}

    def __init__(self):
        self.load()

    def all(self):
        """Returns the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        with open(self.__file_path, "w") as f:
            json.dump(self.__objects, f, indent=4)

    def reload(self):
        """Deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists ;
        otherwise, do nothing. If the file doesn’t exist
        , no exception should be raised)."""
        try:
            with open(self.__file_path, "r") as f:
                self.__objects = json.load(f)
        except FileNotFoundError:
            pass
