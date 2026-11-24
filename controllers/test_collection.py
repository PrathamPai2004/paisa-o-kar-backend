from fastapi import status as status
from fastapi.requests import Request
from fastapi.responses import JSONResponse

async def get_collection(request:Request):
    try:
        q_params = request.query_params

        col_name = q_params.get("col_name")
        db = request.app.state.mongo_db
        collection = db[col_name]
        collections = await db.list_collection_names()

        if col_name not in collections:
            return JSONResponse(
                status_code=status.HTTP_400_BAD_REQUEST,
                content={
                    "message":"Database collection not found",
                    "data":{
                        "collection_name":col_name
                    }
                }
            )
        return status.HTTP_200_OK

    except Exception as e:
        raise