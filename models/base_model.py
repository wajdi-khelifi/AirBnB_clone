#!/usr/bin/python3
"""Base class for all Models"""
import uuid
from datetime import datetime

class BaseModel():
    """All Classes for BaseModel"""

    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items()
            if key == 'created_at' or key == 'updated_at':
                setattr(self, key, datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f'))
            elif key !='__class__':
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
