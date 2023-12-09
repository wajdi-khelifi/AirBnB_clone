#!/usr/bin/python3
"""File Storage"""
import json
from models.base_model import BaseModel


class FileStorage:
    """Manage storage"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionqry __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the Json file"""
        obj_dic = {}
        for key in self.__objects.keys():
            obj = self.__objects[key]
            obj_dic[key] = obj.to_dict()

        with open(self.__file_path, "w") as f:
            json.dump(obj_dic, f)

    def reload(self):
        """Deserializes the Json file to __objects"""
        try:
            with open(FileStorage.__file_path, 'r') as file:
                loaded_objects = json.load(file)
            for key, value in loaded_objects.items():
                class_name, obj_id = key.split('.')
                obj_instance = BaseModel(**value)
                FileStorage.__objects[key] = obj_instance
        except FileNotFoundError:
            pass
