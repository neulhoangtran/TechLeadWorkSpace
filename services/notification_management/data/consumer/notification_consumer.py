from core.modules.message_broker.kafka.message_broker_kafka_impl import MessageBrokerKafkaImpl
from ...domain.usecases.receive_payment_success_notifications import RecievePaymentSuccessNotifications


class NotificationConsumer:
    def __init__(self):
        self.kafka = MessageBrokerKafkaImpl()
        self.message = RecievePaymentSuccessNotifications()
        pass

    async def receive_message_from_payment(self):
        result = self.kafka.subscribe('payment_success')
        if result:
            self.message.execute(result)