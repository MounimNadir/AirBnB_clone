#!/usr/bin/python3

from models.base_model import BaseModel

class User(BaseModel):
    """
    class user that handles user's information
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""