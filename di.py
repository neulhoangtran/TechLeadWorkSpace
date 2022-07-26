from kink import di

from services.payment_management.domain.repository.payment_repository import PaymentRepository
from services.payment_management.data.repository.payment_repository_impl import PaymentRepositoryImpl
from services.payment_management.domain.usecases import *

from services.user_management.domain.repository.user_repository import UserRepository
from services.user_management.data.repository.user_repository_impl import UserRepositoryImpl
from services.user_management.domain.usecases import *
from services.house_management.domain.repository.house_repository import HouseRepository
from services.house_management.data.repository.house_repository_impl import HouseRepositoryImpl
from services.house_management.domain.usecases import *

from services.notification_management.domain.repository.notification_repository import NotificationRepository
from services.notification_management.data.repository.notification_repository_impl import NotificationRepositoryImpl

from core.modules.message_broker.kafka.message_broker_kafka_impl import MessageBrokerKafkaImpl
from core.modules.message_broker.message_broker import MessageBroker

async def init_di():
    paymentRepository = PaymentRepositoryImpl()
    di[PaymentRepository] = paymentRepository
    
    houseRepository = HouseRepositoryImpl()
    di[HouseRepository] = houseRepository

    userRepository = UserRepositoryImpl()
    di[UserRepository] = userRepository

    notificationRepository = NotificationRepositoryImpl()
    di[NotificationRepository] = notificationRepository
    
    message_broker_kafka_impl = MessageBrokerKafkaImpl()
    await message_broker_kafka_impl.init()
    
    di[MessageBroker] = message_broker_kafka_impl