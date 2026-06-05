from fastapi import FastAPI
from app.api.routes import router as orders_router
from app.api.auth_routes.auth_routes import router as auth_router

app = FastAPI(title="Orders Service")

app.include_router(auth_router)
app.include_router(orders_router)
