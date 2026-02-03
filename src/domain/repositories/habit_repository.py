"""
Repository module for habit-related data operations.
"""
from uuid import UUID
from typing import Protocol

from src.domain.entities.habit import Habit

class HabitRepository(Protocol):
    """
    Interface for habit repository operations.
    """
    def get_habit_by_id(self, habit_id: UUID)-> Habit:
        """
        Retrieve a habit by its ID.
        """
        raise NotImplementedError
    
    def save_habit(self, habit: Habit):
        """
        Save or update a habit in the repository.
        """
        raise NotImplementedError