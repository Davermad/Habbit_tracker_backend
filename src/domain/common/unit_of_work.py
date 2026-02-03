"""
Unit of Work pattern for managing database transactions.
"""

from abc import ABC, abstractmethod
from typing import Any  

class UnitOfWork(ABC):
    """
    Abstract base class for Unit of Work pattern.
    """

    @abstractmethod
    def __enter__(self) -> "UnitOfWork":
        """
        Enter the runtime context related to this object.
        """
        pass

    @abstractmethod
    def __exit__(self, exc_type: Any, exc_value: Any, traceback: Any) -> None:
        """
        Exit the runtime context and handle transaction commit or rollback.
        """
        pass

    @abstractmethod
    def commit(self) -> None:
        """
        Commit the current transaction.
        """
        pass

    @abstractmethod
    def rollback(self) -> None:
        """
        Rollback the current transaction.
        """
        pass