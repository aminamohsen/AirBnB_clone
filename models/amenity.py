#!/usr/bin/python3
"""defines the Amenity class"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """represent an amenity

    Attributes:
        name (str): The name of the amenity
    """

    name = ""
