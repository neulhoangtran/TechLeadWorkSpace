class Notification:
    def __init__(self, id: int, userId: int, note: str, houseId: int, bookingId: int, paymentId: int, type: int, content: str, *args, **kwargs) -> None:
        self.id = id
        self.userId = userId
        self.note = note
        self.houseId = houseId
        self.bookingId = bookingId
        self.paymentId = paymentId
        self.type = type
        self.content = content
