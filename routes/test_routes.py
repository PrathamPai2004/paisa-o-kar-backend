from fastapi import APIRouter, Request
from controllers.test_collection import get_collection

test_route = APIRouter(prefix="/v1/test")

@test_route.get("/test-db")
async def get_collection_route(request:Request):
    return await get_collection(request)