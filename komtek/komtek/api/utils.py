"""Some logic functions from views.py"""

def paginate(viewset, queryset):
    """Default Django Rest pagination for viewsets"""
    page = viewset.paginate_queryset(queryset)
    if page is not None:
        serializer = viewset.get_serializer(page, many=True)
        return viewset.get_paginated_response(serializer.data)
    serializer = viewset.get_serializer(queryset, many=True)
    return serializer.data