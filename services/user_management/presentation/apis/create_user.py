from fastapi import APIRouter, Depends
from core.types.failure import Failure

from services.user_management.domain.entities.user import User

from ...domain.usecases.create_user import CreateUser as CreateBaseUserUsecaseImpl

from ...domain.usecases.send_user_to_queue import SendUserToQueue as SendUserToQueueUsecaseImpl


create_user_router = APIRouter()


@create_user_router.post('/create_user/')
async def create_user(
    user = 'test',
    create_new_user: CreateBaseUserUsecaseImpl = Depends(CreateBaseUserUsecaseImpl),
    send_user_to_queue: SendUserToQueueUsecaseImpl = Depends(SendUserToQueueUsecaseImpl)):
    new_user = await create_new_user.execute(user)
    if not type(new_user) is Failure:
        await send_user_to_queue.execute('user_success', new_user)
    return new_user