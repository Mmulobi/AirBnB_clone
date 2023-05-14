#!/usr/bin/python3
"""This is a user class, subclass of BaseModel
"""

from models.base_model import BaseModel
import json


class User(BaseModel):
    '''A subclass of BaseModel class'''

    email = ""
    password = ""
    first_name = ""
    last_name = ""
