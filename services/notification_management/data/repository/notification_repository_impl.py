from fastapi import Depends
from ..dao.notification_dao import NotificationDAO
from ...domain.repository.notification_repository import NotificationRepository
from core.modules.message_broker.kafka.consumer_service import ConsumeService
from kink import inject

@inject
class NotificationRepositoryImpl(NotificationRepository):
    def __init__(self, messageBroker = ConsumeService) -> None:
        super().__init__()
        self.messageBroker = messageBroker
        self.notification_dao = NotificationDAO(1, 1, 'test', 1, 1, 1, 1, 'test')

    async def create_notification(self, notification):
        # Access to db here to create notification then return new notification json object
        return NotificationDAO.from_json({
            'id': notification.id,
            'user_id': notification.status,
            'note': notification.note,
            'booking_id': notification.bookindId,
            'payment_id': notification.paymentId,
            'type': notification.type,
            'content': notification.content
        })

    async def recieve_payment_success_notifications(self, topic):
        result = self.messageBroker.subscribe(topic=topic)
        return result
    
    async def recieve_house_success_notifications(self, topic):
        result = self.messageBroker.subscribe(topic=topic)
        return result
