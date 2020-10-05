from datetime import datetime

from rest_framework import viewsets

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


"""Defining the allowed request methods for each ModelViewSet"""
catalogs = CatalogsViewset.as_view({
    "get": "list",
    "post": "create",
})
elements = ElementsViewset.as_view({
    "get": "list",
    "post": "create",
})