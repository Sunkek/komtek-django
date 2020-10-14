from rest_framework.views import exception_handler
from django.http import HttpResponseBadRequest

from komtek.api.models import Catalog, Element

def custom_exception_handler(exc, context):
    """Custom handler to make more verbose error responses"""
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)
    print("EXCEPTION")
    # Catalog with specified parameters doesn't exist
    if isinstance(exc, Catalog.DoesNotExist):
        err_data = {"MSG_HEADER": "Справочника с указанными названием и версией не существует."}
        response = response or HttpResponseBadRequest(err_data)
    # Element doesn't exist in specified catalog
    if isinstance(exc, Element.DoesNotExist):
        err_data = {"MSG_HEADER": "Элемента с указанными кодом и значением не существует в этом справочнике."}
        response = response or HttpResponseBadRequest(err_data)

    return response