import uvicorn

from fastapi import FastAPI
from di import init_di

from services.payment_management.presentation.apis.get_payment import get_payment_router
from services.payment_management.presentation.apis.create_payment import create_payment_router
from services.user_management.presentation.apis.get_user import get_user_router
from services.user_management.presentation.apis.create_user import create_user_router

from services.house_management.presentation.apis.get_house import get_house_router
from services.house_management.presentation.apis.create_house import create_house_router

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    await init_di()


app.include_router(get_payment_router)
app.include_router(create_payment_router)

app.include_router(get_user_router)
app.include_router(create_user_router)

app.include_router(get_house_router)
app.include_router(create_house_router)

# uvicorn.run(app)