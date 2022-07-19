from typing import Tuple

from core.types.failure import Failure
from ..entities.payment import Payment


class PaymentRepository:

    async def get_payment_by_id(self, id) -> Tuple[Payment, Failure]:
        raise NotImplementedError()

    async def create_payment(self, str) -> Tuple[Payment, Failure]:
        raise NotImplementedError()

    async def send_payment_to_queue(self, topic, payment):
        raise NotImplementedError()

        