"""Some logic functions from views.py"""

VERSION_PADDING = 2  # How many numbers should versions and subversions have

def paginate(viewset, queryset):
    """Default Django Rest pagination for viewsets"""
    page = viewset.paginate_queryset(queryset)
    if page is not None:
        serializer = viewset.get_serializer(page, many=True)
        return viewset.get_paginated_response(serializer.data)
    serializer = viewset.get_serializer(queryset, many=True)
    return serializer.data

def format_version(string):
    """Format version input from 1.1 to 01.01.00"""
    version = [i.zfill(2) for i in string.split(".")] + ["00", "00"]
    return ".".join(version[:3])
