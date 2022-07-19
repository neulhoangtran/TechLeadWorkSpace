class Payment:
    def __init__(self, id: int, paymentStatus: int, note: str, bookingId:int, *args, **kwargs) -> None:
        self.id = id
        self.paymentStatus = paymentStatus
        self.note = note
        self.bookingId = bookingId
