from typing import Tuple

from core.types.failure import Failure
from ..entities.house import House


class HouseRepository:

    async def get_house_by_id(self, id) -> Tuple[House, Failure]:
        raise NotImplementedError()

    async def create_house(self, str) -> Tuple[House, Failure]:
        raise NotImplementedError()

    async def send_house_to_queue(self, topic, house):
        raise NotImplementedError()

        