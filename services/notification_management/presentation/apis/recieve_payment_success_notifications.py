from fastapi import APIRouter, Depends

from ...domain.usecases.receive_payment_success_notifications import RecievePaymentSuccessNotifications

RecievePaymentSuccessNotifications.execute('payment_success')