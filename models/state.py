#!/usr/bin/python3
"""
This is a state class, a subclass of BaseModel
"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    A subclass of BaseModel class with
    Public class attribute:
        name: (str)
    """
    name = ""
