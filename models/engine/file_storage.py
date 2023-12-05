#!/usr/bin/python3
"""FileStorage module - Manage storage"""
import json


class FileStorage:
    """Manage storage"""

    def __init__(self):
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        serialized_objects = {}
        for key, obj in self.__objects.items():
            serialized_objects[key] = obj.to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r') as file:
                loaded_objects = json.load(file)
            for key, value in loaded_objects.items():
                class_name, obj_id = key.split('.')
                obj_instance = models[class_name](**value)
                self.__objects[key] = obj_instance
        except FileNotFoundError:
            pass
