"""
User entity module.
"""

class User:
    """
    User entity representing a user in the system.
    """
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email