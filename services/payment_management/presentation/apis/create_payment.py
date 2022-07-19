from fastapi import APIRouter, Depends
from core.types.failure import Failure

from services.payment_management.domain.entities.payment import Payment

from ...domain.usecases.create_payment import CreatePayment as CreateBasePaymentUsecaseImpl

from ...domain.usecases.send_payment_to_queue import SendPaymentToQueue as SendPaymentToQueueUsecaseImpl


create_payment_router = APIRouter()


@create_payment_router.post('/create_payment/')
async def create_payment(
    payment = 'test',
    create_new_payment: CreateBasePaymentUsecaseImpl = Depends(CreateBasePaymentUsecaseImpl),
    send_payment_to_queue: SendPaymentToQueueUsecaseImpl = Depends(SendPaymentToQueueUsecaseImpl)):
    new_payment = await create_new_payment.execute(payment)
    if not type(new_payment) is Failure:
        await send_payment_to_queue.execute('payment_success', new_payment)
    return new_payment