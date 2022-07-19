from fastapi import APIRouter, Depends

from ...domain.usecases.get_house_by_id import GetHouse as GetBaseHouseUsecaseImpl


get_house_router = APIRouter()


@get_house_router.get('/house/{id}')
async def get_house_by_id(id: str, house: GetBaseHouseUsecaseImpl = Depends(GetBaseHouseUsecaseImpl)):
    result = await house.execute(id)
    return result