"""
Achievement domain service module.
"""
from datetime import date

from src.domain.entities.habit import Habit
from src.domain.entities.reward import Reward
from src.domain.events.reward_achieved import RewardAchievedEvent   

class AchievementService:
    """
    Service for handling achievements.
    """
    def calculate_new_rewards(
        self,
        habit: Habit,
        rewards: list[Reward],
        achievement_date: date
        ) -> list[Reward]:
        """
        Calculate new rewards achieved based on the habit's current streak.
        :param habit: The habit entity.
        :param rewards: List of all possible rewards.
        :return: List of newly achieved rewards.
        """
        newly_achieved_rewards = []
        for reward in rewards:
            if (
                habit.current_streak >= reward.condition_value
                and reward.id not in habit.achieved_rewards_ids
            ):
                newly_achieved_rewards.append(reward)
                habit.achieved_rewards_ids.append(reward.id)
                habit.events.append(RewardAchievedEvent(
                    reward_id=reward.id,
                    user_id=habit.user_id,
                    achievement_date=achievement_date  
                ))
        return newly_achieved_rewards   
