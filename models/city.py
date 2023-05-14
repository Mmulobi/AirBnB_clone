#!/usr/bin/python3
"""
This is a city class, a subclass of BaseModel
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    A subclass of BaseModel class with
    Public class attributes:
        state_id: (str) will be State.id
        name:     (str)
    """
    state_id = ""
    name = ""
