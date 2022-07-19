from fastapi import APIRouter, Depends
from core.types.failure import Failure

from services.notification_management.domain.entities.notification import Notification

from ...domain.usecases.create_notification import CreateNotification as CreateBaseNotificationUsecaseImpl



create_notification_router = APIRouter()


@create_notification_router.post('/notification/')
async def create_notification(
    notification: Notification,
    create_new_notification: CreateBaseNotificationUsecaseImpl = Depends(CreateBaseNotificationUsecaseImpl)):
    new_notification = await create_new_notification.execute(notification)
    return new_notification