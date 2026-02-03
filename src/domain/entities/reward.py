"""
Reward entity module.
"""
from uuid import UUID

class Reward:
    def __init__(
        self, id: UUID, user_id: UUID, name: str, description: str, condition_value: int
        ):
        self.id = id
        self.user_id = user_id
        self.name = name
        self.description = description
        self.condition_value = condition_value
        
