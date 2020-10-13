from rest_framework.views import exception_handler

def custom_exception_handler(exc, context):
    """Custom handler to make more verbose error responses"""
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)
    print("EXCEPTION")
    print(exc.detail)
    print(exc.get_codes())
    print(exc.get_full_details())

    return response