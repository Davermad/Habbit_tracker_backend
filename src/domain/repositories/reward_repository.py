"""
Repository module for reward-related data operations.
"""
from uuid import UUID
from typing import Protocol

from src.domain.entities.reward import Reward

class RewardRepository(Protocol):
    """
    Interface for reward repository operations.
    """
    def get_reward_by_id(self, reward_id: UUID) -> Reward:
        """
        Retrieve a reward by its ID.
        """
        raise NotImplementedError
    
    def get_all_rewards(self, user_id: UUID) -> list[Reward]:
        """
        Retrieve all rewards for a specific user.
        """
        raise NotImplementedError
    
    def save_reward(self, reward: Reward):
        """
        Save or update a reward in the repository.
        """
        raise NotImplementedError