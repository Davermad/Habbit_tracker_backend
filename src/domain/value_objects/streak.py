"""
Streak value object module.
"""

class Streak:
    """
    Value object representing a habit streak.
    """

    def __init__(self, current_streak: int = 0):
        self.current_streak = current_streak

    def increment(self):
        """
        Increment the streak by 1.
        """
        self.current_streak += 1

    def reset(self):
        """
        Reset the streak to 0.
        """
        self.current_streak = 0