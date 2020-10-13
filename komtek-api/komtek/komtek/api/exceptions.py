from rest_framework.views import exception_handler
from django.db.models.Model import DoesNotExist

def custom_exception_handler(exc, context):
    """Custom handler to make more verbose error responses"""
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)
    print("EXCEPTION")
    if isinstance(exc, DoesNotExist):
        print(exc.__dict__)

    return response