from email import message

from fastapi import Depends
from ..dao.payment_dao import PaymentDAO
from ...domain.repository.payment_repository import PaymentRepository
# from core.modules.message_broker.message_broker import MessageBroker
from core.modules.message_broker.kafka.message_broker_kafka_impl import MessageBrokerKafkaImpl
from kink import inject

@inject
class PaymentRepositoryImpl(PaymentRepository):
    def __init__(self, messageBroker = MessageBrokerKafkaImpl) -> None:
        super().__init__()
        self.messageBroker = messageBroker
        self.payment_dao = PaymentDAO(1, 1, 'test', 1)

    async def get_payment_by_id(self, id):
        # Access to db here
        return PaymentDAO.from_json({
            'payment_status': 1,
            'note': 'test note',
            'booking_id': 1
        })

    async def create_payment(self, str):
        # Access to db here to create payment then return new payment json object
        return PaymentDAO.from_json({
            'payment_status': 1,
            'note': 'test',
            'booking_id': 1
        })
    
    async def send_payment_to_queue(self, topic, payment):
        await self.messageBroker.send(topic=topic, service=payment)
