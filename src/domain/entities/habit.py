"""
Habit Entity Module
"""
from uuid import UUID
from datetime import datetime, timedelta, timezone

from src.domain.exceptions import HabitIsAlreadyCompletedException

class Habit:
    """
    Represents a habit with a name and description.
    """
    
    def __init__(
        self, id: UUID, user_id: UUID, name: str, description: str, current_streak: int, date_created: datetime, date_of_last_completion: datetime = None
        ):
        self.id = id
        self.user_id = user_id
        self.name = name
        self.description = description
        self.current_streak = current_streak
        self.dage_created = date_created
        self.date_of_last_completion = date_of_last_completion
        
    def is_habit_completed_today(self, today_date: str) -> bool:
       """
       Check if the habit was completed today.
       :param today_date: The date to check against.
       :return: True if the habit was completed today, otherwise False.
       """
       if not (self.date_of_last_completion == today_date):
           raise HabitIsAlreadyCompletedException("Habit is already completed today.")
       return True
   
    def is_loose_streak(self) -> bool:
        """
        Check if the habit streak is lost.
        :return: True if the habit streak is lost, otherwise False.
        """
        if (self.date_of_last_completion < (datetime.now(timezone.utc) - timedelta(days=1)).strftime("%Y-%m-%d")):
           return True
        return False
    
    # Не понимаю как реализовать сбор событий 
        