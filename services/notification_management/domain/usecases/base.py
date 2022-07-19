from kink import inject

from ..repository.notification_repository import NotificationRepository


@inject
class BaseNotificationUsecase:
    def __init__(self, repository: NotificationRepository) -> None:
        self.repository = repository