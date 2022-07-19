from ...domain.entities.payment import Payment


class PaymentDAO(Payment):
    def __init__(self, id: int, paymentStatus: int, note: str, bookingId: int, *args, **kwargs) -> None:
        super().__init__(id, paymentStatus, note, bookingId, *args, **kwargs)

    @staticmethod
    def from_json(json_data) -> Payment:
        return Payment(1, json_data['payment_status'], json_data['note'], json_data['booking_id'])