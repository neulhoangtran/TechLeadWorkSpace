from .base import BasePaymentUsecase


class SendPaymentToQueue(BasePaymentUsecase):
    def __init__(self) -> None:
        super().__init__()

    async def execute(self, topic, payment):
        return await self.repository.send_payment_to_queue(topic, payment)