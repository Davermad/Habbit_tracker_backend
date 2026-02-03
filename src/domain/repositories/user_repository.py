"""
Repository module for user-related data operations.
"""
from uuid import UUID
from typing import Protocol

from src.domain.entities.user import User

class UserRepository(Protocol):
    """
    Interface for user repository operations.
    """
    def get_user_by_id(self, user_id: UUID) -> User:
        """
        Retrieve a user by their ID.
        """
        raise NotImplementedError
    
    def save_user(self, user: User):
        """
        Save or update a user in the repository.
        """
        raise NotImplementedError