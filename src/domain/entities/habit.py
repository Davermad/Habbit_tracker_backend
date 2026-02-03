"""
Habit Entity Module
"""
from uuid import UUID
from datetime import timedelta, date

from src.domain.exceptions import HabitIsAlreadyCompletedException
from src.domain.events.habit_completed import HabitCompletedEvent
from src.domain.events.streak_broken import StreakBrokenEvent
from src.domain.value_objects.streak import Streak

class Habit:
    """
    Represents a habit with a name and description.
    """
    
    def __init__(
        self, id: UUID, user_id: UUID, name: str, description: str, current_streak: Streak, date_created: date, date_of_last_completion: date = None, achieved_rewards_ids: list[UUID] = None
        ):
        self.id = id
        self.user_id = user_id
        self.name = name
        self.description = description
        self.current_streak = current_streak
        self.date_created = date_created
        self.date_of_last_completion = date_of_last_completion
        self.achieved_rewards_ids = achieved_rewards_ids or []
        self.events = []
        
    def is_habit_completed_today(self, today_date: date) -> bool:
       """
       Check if the habit was completed today.
       :param today_date: The date to check against.
       :return: True if the habit was completed today, otherwise False.
       """
       if self.date_of_last_completion is None:
           return False
       if (self.date_of_last_completion == today_date):
           raise HabitIsAlreadyCompletedException("Habit is already completed today.")
       return False
   
    def check_streak_status(self, current_date: date) -> bool:
        """
        Check if the habit streak is lost.
        :return: True if the habit streak is lost, otherwise False.
        """
        if self.date_of_last_completion is None:
            return False
        if (self.date_of_last_completion < current_date - timedelta(days=1)):
           return True
        return False
    
    def complete_habit(self, completion_date: date):
        """
        Complete the habit for the given date.
        """
        if self.is_habit_completed_today(completion_date):
            raise HabitIsAlreadyCompletedException("Habit is already completed today.")
        
        if self.check_streak_status(completion_date):
            self.current_streak.reset()
            self.current_streak.increment()
            self.events.append(StreakBrokenEvent(
                habit_id=self.id,
                user_id=self.user_id,
                broken_date=completion_date
            ))
        else:
            self.current_streak.increment()
        
        self.date_of_last_completion = completion_date
        
        self.events.append(HabitCompletedEvent(
            habit_id=self.id,
            user_id=self.user_id,
            completion_date=completion_date
        ))
        