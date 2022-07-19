from fastapi import APIRouter, Depends

from ...domain.usecases.get_payment_by_id import GetPayment as GetBasePaymentUsecaseImpl


get_payment_router = APIRouter()


@get_payment_router.get('/payment/{id}')
async def get_payment_by_id(id: str, payment: GetBasePaymentUsecaseImpl = Depends(GetBasePaymentUsecaseImpl)):
    result = await payment.execute(id)
    return result