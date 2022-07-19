from typing import Tuple

from core.types.failure import Failure
from ..message_broker import MessageBroker
from .producer_service import ProducerService
from .consumer_service import ConsumeService

class MessageBrokerKafkaImpl(MessageBroker):
    def __init__(self) -> None:
        super().__init__()
    
    async def send(topic, payment) -> Tuple[bool, Failure]:
        return ProducerService.send(topic, payment, None)
    
    async def send_house(topic, house) -> Tuple[bool, Failure]:
        return ProducerService.send(topic, house, None)

    async def subscribe(self, topic) -> Tuple[bool, Failure]:
        return ConsumeService.subscribe(topic)