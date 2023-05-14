#!/usr/bin/python3
"""
This is a review class, a subclass of BaseModel class
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    A subclass of BaseModel class with
    Public class attributes:
        place_id:            (str) will be Place.id
        user_id:             (str) will be User.id
        text:                (str)
    """
    place_id = ""
    user_id = ""
    text = ""
