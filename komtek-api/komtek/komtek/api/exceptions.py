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
        response = response or HttpResponseBadRequest(
            "Справочника с указанными названием и версией не существует."
        )
    # Element doesn't exist in specified catalog
    if isinstance(exc, Element.DoesNotExist):
        response = response or HttpResponseBadRequest(
            "Элемента с указанными кодом и значением не существует в этом справочнике."
        )

    return response