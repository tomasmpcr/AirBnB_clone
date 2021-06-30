#!/usr/bin/python3
"""
Defines class ``User``:
inherits from class object BaseModel
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    class object to define attributes/method of each instance of user
    """
    email = ''
    password = ''
    first_name = ''
    last_name = ''

    def __init__(self, *args, **kwargs):
        """class constructor"""
        super().__init__()
