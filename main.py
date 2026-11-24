from contextlib import asynccontextmanager
from fastapi import FastAPI
from core.config import settings
from fastapi.middleware.cors import CORSMiddleware
from database.mongodb import connect_mongodb,get_mongodb

from routes.test_routes import test_route

@asynccontextmanager
async def lifespan(app:FastAPI):
    try:
        print("Startup happening...")
        await connect_mongodb()
        print("Databases are Up")
        app.state.mongo_db = get_mongodb()

        yield
        print("Shutdown happening...")

    except Exception as e:
        raise

app = FastAPI(
    title=settings.APP_NAME,
    lifespan=lifespan
)

app.include_router(test_route)