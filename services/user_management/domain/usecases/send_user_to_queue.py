from .base import BaseUserUsecase


class SendUserToQueue(BaseUserUsecase):
    def __init__(self) -> None:
        super().__init__()

    async def execute(self, topic, user):
        return await self.repository.send_user_to_queue(topic, user)