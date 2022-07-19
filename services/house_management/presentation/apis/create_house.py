from fastapi import APIRouter, Depends
from core.types.failure import Failure

from services.house_management.domain.entities.house import House

from ...domain.usecases.create_house import CreateHouse as CreateBaseHouseUsecaseImpl

from ...domain.usecases.send_house_to_queue import SendHouseToQueue as SendHouseToQueueUsecaseImpl


create_house_router = APIRouter()


@create_house_router.post('/create_house/')
async def create_house(
    house = 'test',
    create_new_house: CreateBaseHouseUsecaseImpl = Depends(CreateBaseHouseUsecaseImpl),
    send_house_to_queue: SendHouseToQueueUsecaseImpl = Depends(SendHouseToQueueUsecaseImpl)):
    new_house = await create_new_house.execute(house)
    if not type(new_house) is Failure:
        await send_house_to_queue.execute('house_success', new_house)
    return new_house