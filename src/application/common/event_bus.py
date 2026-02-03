"""
Event Bus Protocol
Defines the interface for an event bus that publishes domain events.
"""
from abc import abstractmethod
from typing import Protocol


class EventBus(Protocol):
    @abstractmethod
    async def publish(self, events: list) -> None:
        raise NotImplementedError("Method must be implemented by subclasses")
