from fastapi import Request,Response
from fastapi import status as status
from fastapi.responses import JSONResponse
from core.config import Roles
from utils.validation import validate_email,check_empty_values

async def signup(request:Request):
    try:
        requester_role = request.state.role

        body = await request.json()

        first_name = body.get("full_name")
        last_name = body.get("last_name")
        usn = body.get("usn")
        email = body.get("email")
        phone = body.get("phone")

        check_empty_values = [message for message in ]

        #validation layer 
        email_check = validate_email(email)

        

        auth_result = 
            
        


async def approve(request:Request):
    try:
        requester_role = request.state.role
        if requester_role != Roles.SUPER_ADMIN.value:
            return JSONResponse(
                content={"message":"Forbidden access! "},
                status_code=status.HTTP_403_FORBIDDEN
            )
        else:
            body = await request.json()

            guest_user_id = await body.get("guest_user_id")
            approval_status = await body.get("approval_status")


