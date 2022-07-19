from fastapi import APIRouter, Depends

from ...domain.usecases.receive_user_success_notifications import RecieveUserSuccessNotifications

RecieveUserSuccessNotifications.execute('user_success')