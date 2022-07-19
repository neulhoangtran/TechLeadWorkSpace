from .base import BasePaymentUsecase


class CreatePayment(BasePaymentUsecase):
    def __init__(self) -> None:
        super().__init__()

    async def execute(self, str):
        return await self.repository.create_payment(str)