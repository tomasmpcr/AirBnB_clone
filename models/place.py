#!/usr/bin/python3
"""Module for the Place class
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    place class BaseModel
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
