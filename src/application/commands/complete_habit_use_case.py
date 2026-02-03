"""
Module for the CompleteHabitUseCase class, which handles the logic for completing a habit in the application.
"""
from datetime import date
from uuid import UUID
from src.domain.repositories.habit_repository import HabitRepository
from src.domain.repositories.user_repository import UserRepository
from src.domain.repositories.reward_repository import RewardRepository
from src.domain.services.achievement import AchievementService
from src.domain.common.unit_of_work import UnitOfWork
from src.application.common.event_bus import EventBus

class CompleteHabitUseCase:
    """
    Use case for completing a habit.
    """
    def __init__(
        self,
        habit_repository: HabitRepository,
        user_repository: UserRepository,
        reward_repository: RewardRepository,
        achievement_service: AchievementService,
        uow: UnitOfWork,
        event_bus: EventBus
        
    ):
        self.habit_repository = habit_repository
        self.user_repository = user_repository
        self.reward_repository = reward_repository
        self.event_bus = event_bus
        
        self.achievement_service = achievement_service
        self.uow = uow
        
    async def execute(self, user_id: UUID, habit_id: UUID) -> None:
        """
        Execute the use case to complete a habit.

        :param user_id: ID of the user completing the habit.
        :param habit_id: ID of the habit to be completed.
        """
        with self.uow:
            user = self.user_repository.get_user_by_id(user_id)
            habit = self.habit_repository.get_habit_by_id(habit_id)
            rewards = self.reward_repository.get_all_rewards(user_id)

            if not user or not habit: 
                raise ValueError("User or Habit not found.")
            
            habit.complete_habit(completion_date=date.today()) 
            self.achievement_service.calculate_new_rewards(
                habit=habit,
                rewards=rewards,
                achievement_date=date.today())
            self.uow.commit()
            
            for event in habit.events:
                await self.event_bus.publish(event)
            habit.events.clear()
