import os 
import re
from settings.config import DATABASE_DIR
import json


class User():
    def __init__(self, identifier):
        self.phone = self.email = None
        phone_match = re.match(r'^(\+\d{1,2}\s?)?((\(\d{3}\))|\d{3})[\s.-]?\d{3}[\s.-]?\d{4}$', identifier)
        email_match = re.match(r'^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', identifier)
        
        if phone_match:
            self.phone = identifier
        
        elif email_match:
            self.email = identifier

    def verify(self, not_hashed_password):
        with open(os.path.join(DATABASE_DIR, "user.json")) as file:
            users = json.load(file)

        if self.email:
            for user in users:
                if user["email"] == self.email:
                    if user["password"] == not_hashed_password:
                        return True
                
        elif self.phone:
            for user in users:
                if user["phone"] == self.phone:
                    if user["password"] == not_hashed_password:
                        return True
        
        return False

