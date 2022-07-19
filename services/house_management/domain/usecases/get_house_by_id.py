from .base import BaseHouseUsecase


class GetHouse(BaseHouseUsecase):
    def __init__(self) -> None:
        super().__init__()

    async def execute(self, id):
        return await self.repository.get_house_by_id(id)