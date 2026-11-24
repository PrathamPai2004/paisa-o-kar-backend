from pymongo import AsyncMongoClient
from pymongo.asynchronous.database import AsyncDatabase
from core.config import settings

client : AsyncMongoClient | None = None
database : AsyncDatabase | None = None

#connect mongodb

async def connect_mongodb():
    global client,database

    try:
        client = AsyncMongoClient(
            host=settings.MONGODB_URI,
            serverSelectionTimeoutMS=5000
        )

        await client.admin.command("ping")

        database = client["cse_faculty_portal"]

        print("MongoDB connected successfully")
    except ConnectionError as con_err:
        print(f"MongoDB connection failed: {con_err}")
        raise 

def get_mongodb():

    if database is None:
        raise RuntimeError("MongoDB is not connected")

    return database