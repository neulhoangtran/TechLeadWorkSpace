from email import message

from fastapi import Depends
from ..dao.user_dao import UserDAO
from ...domain.repository.user_repository import UserRepository
# from core.modules.message_broker.message_broker import MessageBroker
from core.modules.message_broker.kafka.message_broker_kafka_impl import MessageBrokerKafkaImpl
from kink import inject

@inject
class UserRepositoryImpl(UserRepository):
    def __init__(self, messageBroker = MessageBrokerKafkaImpl) -> None:
        super().__init__()
        self.messageBroker = messageBroker
        self.user_dao = UserDAO(1, 'first', 'last', '2112343', 'vik', '!Password1', 'test@yopmail.com')

    async def get_user_by_id(self, id):
        # Access to db here
        return UserDAO.from_json({
            'id': 1,
            'first_name': 'first',
            'last_name': 'last',
            'phone_number': '2112343',
            'user_name': 'vik',
            'password': '!Password1',
            'email': 'test@yopmail.com'
        })

    async def create_user(self, str):
        # Access to db here to create user then return new user json object
        return UserDAO.from_json({
            'id': 1,
            'first_name': 'first',
            'last_name': 'last',
            'phone_number': '2112343',
            'user_name': 'vik',
            'password': '!Password1',
            'email': 'test@yopmail.com'
        })
    
    async def send_user_to_queue(self, topic, user):
        await self.messageBroker.send(topic=topic, user=user)
