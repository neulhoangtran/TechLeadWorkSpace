from email import message

from fastapi import Depends
from ..dao.house_dao import HouseDAO
from ...domain.repository.house_repository import HouseRepository
# from core.modules.message_broker.message_broker import MessageBroker
from core.modules.message_broker.kafka.message_broker_kafka_impl import MessageBrokerKafkaImpl
from kink import inject

@inject
class HouseRepositoryImpl(HouseRepository):
    def __init__(self, messageBroker = MessageBrokerKafkaImpl) -> None:
        super().__init__()
        self.messageBroker = messageBroker
        self.house_dao = HouseDAO(
            1,
            1,
            'Viet Nam',
            'HCM',
            'Quan 7',
            'Ba Trieu',
            'my note',
            1,
            1
        )

    async def get_house_by_id(self, id):
        # Access to db here
        return HouseDAO.from_json({
            'owner_id': 1,
            'country': 'Viet Nam',
            'city': 'Ha Noi',
            'district': 'Cau Giay',
            'address_detail': 'Duong Dinh Nghe',
            'note': 'my note',
            'house_status': 1,
            'house_type_id': 1
        })
        
    async def create_house(self, str):
        # Access to db here to create house then return new house json object
        return HouseDAO.from_json({
            'owner_id': 1,
            'country': 'Viet Nam',
            'city': 'HCM',
            'district': 'Quan 7',
            'address_detail': 'Ba Trieu',
            'note': 'my note',
            'house_status': 1,
            'house_type_id': 1
        })
    
    async def send_house_to_queue(self, topic, house):
        await self.messageBroker.send(topic=topic, service=house)
