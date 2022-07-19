from .base import BaseHouseUsecase


class CreateHouse(BaseHouseUsecase):
    def __init__(self) -> None:
        super().__init__()

    async def execute(self, str):
        return await self.repository.create_house(str)