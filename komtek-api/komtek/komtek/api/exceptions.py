from rest_framework.views import exception_handler
from komtek.api.models import Catalog

def custom_exception_handler(exc, context):
    """Custom handler to make more verbose error responses"""
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)
    print("EXCEPTION")
    # Catalog with specified parameters doesn't exist
    if isinstance(exc, Catalog.DoesNotExist):
        pass
    # Element doesn't exist in specified catalog
    # Element exists, but its description is different

    return response