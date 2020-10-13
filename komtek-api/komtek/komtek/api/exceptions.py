from rest_framework.views import exception_handler

def custom_exception_handler(exc, context):
    """Custom handler to make more verbose error responses"""
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)
    print("EXCEPTION")
    print("exc")
    print(type(exc))
    print(exc.__dict__)
    print(type(context))
    print(context.__dict__)

    return response