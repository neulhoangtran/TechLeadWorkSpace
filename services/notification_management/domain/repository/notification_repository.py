import string
from typing import Tuple

from core.types.failure import Failure
from ..entities.notification import Notification


class NotificationRepository:

    async def create_notification(self, notificaiton) -> Tuple[Notification, Failure]:
        raise NotImplementedError()

    async def recieve_payment_success_notifications(self, topic) -> Tuple[str, Failure]:
        raise NotImplementedError()
    
    async def recieve_house_success_notifications(self, topic) -> Tuple[str, Failure]:
        raise NotImplementedError()

    async def recieve_user_success_notifications(self, topic) -> Tuple[str, Failure]:
        raise NotImplementedError()
