"""
Docstring for domain.exceptions
"""

class HabitIsAlreadyCompletedException(Exception):
    """
    Exception raised when trying to complete a habit that has already been completed for the day.
    """
    pass