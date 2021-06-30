#!/usr/bin/python3
"""
BaseModel that defines all common attributes/methods for other classes
"""


import json
import uuid
from datetime import datetime
import models


class BaseModel:
    """
    base class
    """

    def __init__(self, *args, **kwargs):
        """
        define init
        """
        date = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            self.created_at = datetime.strptime(kwargs["created_at"], date)
            self.updated_at = datetime.strptime(kwargs["updated_at"], date)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            models.storage.new(self)
            models.storage.save()

    def __str__(self):
        """
        string representation of the BaseModel class
        """
        return "[{}] ({}) {}".\
            format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Updates updated_at with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all keys or values of dict
        """
        ndict = self.__dict__.copy()
        ndict['__class__'] = self.__class__.__name__
        ndict['updated_at'] = self.updated_at.isoformat()
        ndict['created_at'] = self.created_at.isoformat()
        return ndict
