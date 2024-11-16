from fastapi import FastAPI

from src.items.router import router as items_router
from src.types.router import router as types_router

app = FastAPI(
    title='Vkusno'
)

app.include_router(items_router)
app.include_router(types_router)