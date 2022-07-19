from fastapi import Depends
from services.notification_management.domain.repository.notification_repository import NotificationRepository
from .base import BaseNotificationUsecase


class RecievePaymentSuccessNotifications(BaseNotificationUsecase):
    def __init__(self, repository: NotificationRepository = Depends(NotificationRepository)) -> None:
        super().__init__()
        self.repository = repository

    async def execute(self, topic):
        return await self.repository.recieve_payment_success_notifications(topic)