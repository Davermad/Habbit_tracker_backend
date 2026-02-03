"""
Reward Achieved Event module.
"""

class RewardAchievedEvent:
    """
    Event representing the achievement of a reward.
    """
    def __init__(
        self,
        reward_id,
        user_id,
        achievement_date
    ):
        self.reward_id = reward_id
        self.user_id = user_id
        self.achievement_date = achievement_date