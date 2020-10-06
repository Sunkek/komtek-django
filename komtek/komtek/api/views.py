from datetime import date as dt_date
from datetime import datetime

from django.db.models import Q
from rest_framework import viewsets
from rest_framework.response import Response

import komtek.api.utils as utils
from .models import Catalog, Element
from .serializers import CatalogSerializer, ElementSerializer


class CatalogsViewset(viewsets.ModelViewSet):
    """Display all catalogs"""
    queryset = Catalog.objects.all().order_by('-date_created')
    serializer_class = CatalogSerializer


class ElementsViewset(viewsets.ModelViewSet):
    """Show all or specific version catalog elements"""
    queryset = Element.objects.all().order_by('-date_created')
    serializer_class = ElementSerializer


class CatalogsActualViewset(viewsets.ModelViewSet):
    """Display only the catalogs that were created before the specific date
    and didn't expire before it. Passing no date results in catalogs that are
    actual for today."""
    queryset = Catalog.objects.all().order_by('-date_created')
    serializer_class = CatalogSerializer
        
    def list(self, request, date=None, *args, **kwargs):
        """Rewriting the default list function"""
        date = datetime.strptime(date, "%d-%m-%Y") if date else dt_date.today()
        catalogs = Catalog.objects.all().order_by("-date_created")
        catalogs = catalogs.filter(date_released__lte=date)
        catalogs = catalogs.filter(Q(date_expired__gt=date) | Q(date_expired=None))
        return Response(utils.paginate(self, catalogs))


class ElementsByCatalogViewset(viewsets.ModelViewSet):
    """Display only the elements of a selected catalog by its name and version"""
    queryset = Element.objects.all().order_by('-date_created')
    serializer_class = ElementSerializer
        
    def get_queryset(self):
        """Overriding the default get_queryset for clarity"""
        elements = Element.objects.all().order_by("code")
        catalog_name = self.request.query_params.get("catalog_name")
        catalog_version = self.request.query_params.get("catalog_version")
        elements = elements.filter(catalog__short_name=catalog_name)
        elements = elements.filter(catalog__version=catalog_version)
        return elements


"""Defining the allowed request methods for each ModelViewSet"""
catalogs = CatalogsViewset.as_view({
    "get": "list",
    "post": "create",
})
elements = ElementsViewset.as_view({
    "get": "list",
    "post": "create",
})
catalogs_actual = CatalogsActualViewset.as_view({
    "get": "list",
})
elements_by_catalog = ElementsByCatalogViewset.as_view({
    "get": "list",
})