from typing import Tuple
from core.types.failure import Failure

class MessageBroker:

    async def send(self, topic, payment) -> Tuple[bool, Failure]:
        raise NotImplementedError()

    async def subscribe(self, topics) -> Tuple[bool, Failure]:
        raise NotImplementedError()

    async def init(self):
        pass