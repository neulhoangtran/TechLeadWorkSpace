from .base import BasePaymentUsecase


class GetPayment(BasePaymentUsecase):
    def __init__(self) -> None:
        super().__init__()

    async def execute(self, id):
        return await self.repository.get_payment_by_id(id)