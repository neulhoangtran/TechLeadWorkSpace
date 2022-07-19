from .base import BaseNotificationUsecase


class CreateNotification(BaseNotificationUsecase):
    def __init__(self) -> None:
        super().__init__()

    async def execute(self, notification):
        return await self.repository.create_notification(notification)