from fastapi import APIRouter, Depends

from ...domain.usecases.get_user_by_id import GetUser as GetBaseUserUsecaseImpl


get_user_router = APIRouter()


@get_user_router.get('/user/{id}')
async def get_user_by_id(id: str, user: GetBaseUserUsecaseImpl = Depends(GetBaseUserUsecaseImpl)):
    result = await user.execute(id)
    return result