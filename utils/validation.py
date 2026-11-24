from email_validator import validate_email,EmailNotValidError
from phonenumbers import NumberParseException
import phonenumbers
import re
from core.config import Roles

def check_empty_values(value:str):
    if not value:
        return {
            "message":f"{value} cannot be empty"
        }
    else:
        return False
    
def check_valid_email(email:str):
    try:
        result = validate_email(email,check_deliverability=False)

        return True

    except EmailNotValidError as email_error:
        raise

def check_valid_phone(phone:str):
    try:
        parsed_phone_no = phonenumbers.parse(phone,"IN")

        if not phonenumbers.is_valid_number(parsed_phone_no):
            return {
                "valid":False,
                "message":"Phone number not valid"
            }
        else:
            return {
                "valid":True,
                "message":"Phone number valid"
            }
    except NumberParseException:
        raise

def check_valid_usn(usn:str,role:str):
    try:
        valid_usn = "2SD22CS064"
        student_pattern = r"^2SD\d{2}(CS|IS|EC|EE|ME|CV|AI)\d{3}$"
        if role is Roles.STUDENT.value:
            is_valid_usn = bool(re.match(student_pattern,usn))
            return is_valid_usn
        else:
            alumini_pattern=""  
            print("TBD by arya")
    except Exception as e:
        raise
