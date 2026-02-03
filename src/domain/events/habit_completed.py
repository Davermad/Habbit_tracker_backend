"""
Habit Completed Event
"""
from uuid import UUID
from datetime import date

class HabitCompletedEvent:
    """
    Event representing the completion of a habit.
    """
    def __init__(
        self, 
        habit_id: UUID, 
        user_id: UUID, 
        completion_date: date
        ):
        self.habit_id = habit_id
        self.user_id = user_id
        self.completion_date = completion_date