from .base import BaseUserUsecase


class CreateUser (BaseUserUsecase):
    def __init__(self) -> None:
        super().__init__()

    async def execute(self, str):
        return await self.repository.create_user(str)