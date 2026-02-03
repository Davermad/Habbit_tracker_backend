"""
Streak Broken Event Module
"""
from datetime import date
from uuid import UUID
class StreakBrokenEvent:
    """
    Event representing the breaking of a habit streak.
    """
    def __init__(self, habit_id: UUID, user_id: UUID, broken_date: date):
        self.habit_id = habit_id
        self.user_id = user_id
        self.broken_date = broken_date