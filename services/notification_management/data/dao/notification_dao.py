from ...domain.entities.notification import Notification


class NotificationDAO(Notification):
    def __init__(self, id: int, userId: int, note: str, houseId: int, bookingId: int, paymentId: int, type: int, content: str, *args, **kwargs) -> None:
        super().__init__(id, userId, note, houseId, bookingId, paymentId, type, content, *args, **kwargs)

    @staticmethod
    def from_json(json_data) -> Notification:
        return Notification(1, json_data['user_id'], json_data['note'], json_data['house_id'], json_data['booking_id'], json_data['payment_id'], json_data['type'], json_data['content'])