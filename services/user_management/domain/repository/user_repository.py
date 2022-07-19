from typing import Tuple

from core.types.failure import Failure
from ..entities.user import User


class UserRepository:

    async def get_user_by_id(self, id) -> Tuple[User, Failure]:
        raise NotImplementedError()

    async def create_user(self, str) -> Tuple[User, Failure]:
        raise NotImplementedError()

    async def send_user_to_queue(self, topic, user):
        raise NotImplementedError()
        