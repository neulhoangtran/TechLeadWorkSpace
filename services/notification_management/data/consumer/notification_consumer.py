from core.modules.message_broker.kafka.message_broker_kafka_impl import MessageBrokerKafkaImpl
from ...domain.usecases.receive_payment_success_notifications import RecievePaymentSuccessNotifications
from ...domain.usecases.receive_house_success_notifications import RecieveHouseSuccessNotifications
from ...domain.usecases.receive_user_success_notifications import RecieveUserSuccessNotifications


class NotificationConsumer:
    def __init__(self):
        self.kafka = MessageBrokerKafkaImpl()
        self.message = RecievePaymentSuccessNotifications()
        self.message_house = RecieveHouseSuccessNotifications()
        self.message_user = RecieveUserSuccessNotifications()
        pass

    async def receive_message_from_payment(self):
        result = self.kafka.subscribe('payment_success')
        if result:
            self.message.execute(result)
            
    async def receive_message_from_house(self):
        result = self.kafka.subscribe('house_success')
        if result:
            self.message_house.execute(result)

    async def receive_message_from_user(self):
        result = self.kafka.subscribe('user_success')
        if result:
            self.message_user.execute(result)
