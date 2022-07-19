from kink import inject

from ..repository.payment_repository import PaymentRepository


@inject
class BasePaymentUsecase:
    def __init__(self, repository: PaymentRepository) -> None:
        self.repository = repository