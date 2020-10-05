from datetime import date as dt_date
from datetime import datetime

from django.db.models import Q
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Catalog, Element
from .serializers import CatalogSerializer, ElementSerializer


class CatalogsViewset(viewsets.ModelViewSet):
    """Display all catalogs"""
    queryset = Catalog.objects.all().order_by('-date_created')
    serializer_class = CatalogSerializer


class CatalogsActualViewset(viewsets.ModelViewSet):
    """Display only the catalogs that were created before the specific date
    and didn't expire before it. Passing no date results in catalogs that are
    actual for today."""
    queryset = Catalog.objects.all().order_by('-date_created')
    serializer_class = CatalogSerializer
        
    def list(self, request, date=None, *args, **kwargs):
        date = datetime.strptime(date, "%d-%m-%Y") if date else dt_date.today()
        print(date)
        catalogs = Catalog.objects.all().order_by('-date_created')
        print(catalogs)
        catalogs = catalogs.filter(date_released__lte=date)
        print(catalogs)
        catalogs = catalogs.filter(Q(date_expired__gt=date) | Q(date_expired=None))
        print(catalogs)
        page = self.paginate_queryset(catalogs)
        if page is not None:
            serializer = CatalogSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = CatalogSerializer(catalogs, many=True)
        return Response(serializer.data)

class ElementsViewset(viewsets.ModelViewSet):
    """Show all or specific version catalog elements"""
    queryset = Element.objects.all().order_by('-date_created')
    serializer_class = ElementSerializer

"""Defining the allowed request methods for each ModelViewSet"""
catalogs = CatalogsViewset.as_view({
    "get": "list",
    "post": "create",
})
catalogs_actual = CatalogsActualViewset.as_view({
    "get": "list",
})
elements = ElementsViewset.as_view({
    "get": "list",
    "post": "create",
})