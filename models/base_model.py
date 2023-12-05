#!/usr/bin/python3
"""Base class for all Models"""
import uuid
from datetime import datetime


class BaseModel():
    """All Classes for BaseModel"""

    def __init__(self, *args, **kwargs):
        """Starts a new Model"""
        date_value = '%Y-%m-%dT%H:%M:%S.%f'

        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.strptime(value, date_value))
                elif key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):



    def save(self):
        """Updates the updated_at attribute
        with the current datetime"""

        self.update_at = datetime.now()
        storage.save()


    def to_dic(self):
