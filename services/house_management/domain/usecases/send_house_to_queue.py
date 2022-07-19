from .base import BaseHouseUsecase


class SendHouseToQueue(BaseHouseUsecase):
    def __init__(self) -> None:
        super().__init__()

    async def execute(self, topic, house):
        return await self.repository.send_house_to_queue(topic, house)