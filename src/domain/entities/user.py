"""
User entity module.
"""
from uuid import UUID
class User:
    """
    User entity representing a user in the system.
    """
    def __init__(self, id: UUID, name: str, email: str):
        self.id = id
        self.name = name
        self.email = email