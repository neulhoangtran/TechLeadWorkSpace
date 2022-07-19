from fastapi import APIRouter, Depends

from ...domain.usecases.receive_house_success_notifications import RecieveHouseSuccessNotifications

RecieveHouseSuccessNotifications.execute('house_success')