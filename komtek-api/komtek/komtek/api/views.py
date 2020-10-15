from datetime import date as dt_date
from datetime import datetime
from json import loads

from django.db.models import Q
from rest_framework import viewsets, status
from rest_framework.response import Response

from komtek.api.utils import format_version
from .models import Catalog, Element
from .serializers import CatalogSerializer, ElementSerializer


class CatalogsViewset(viewsets.ModelViewSet):
    """Display all catalogs"""
    queryset = Catalog.objects.all().order_by('-date_created')
    serializer_class = CatalogSerializer
    
    def perform_create(self, serializer):
        data = serializer.validated_data
        serializer.save(version=format_version(data["version"]))


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
        
    def get_queryset(self):
        """Overriding the default get_queryset to select actual catalogs"""
        date = self.request.parser_context["kwargs"].get("date")
        date = datetime.strptime(date, "%d-%m-%Y") if date else dt_date.today()
        catalogs = Catalog.objects.all().order_by("-date_created")
        catalogs = catalogs.filter(date_started__lte=date)
        catalogs = catalogs.filter(Q(date_expired__gt=date) | Q(date_expired=None))
        return catalogs


class ElementsByCatalogViewset(viewsets.ModelViewSet):
    """Display only the elements of a selected catalog by its name and version"""
    queryset = Element.objects.all().order_by('-date_created')
    serializer_class = ElementSerializer
        
    def get_queryset(self):
        """Overriding the default get_queryset for clarity"""
        elements = Element.objects.all().order_by("code")
        catalog_name = self.request.query_params.get("catalog_name", "")
        catalog_version = self.request.query_params.get("catalog_version", "")
        if catalog_name and not catalog_version:
            catalog = Catalog.objects.filter(
                short_name=catalog_name,
                date_started__lte=dt_date.today()
            )
            catalog = catalog.latest("date_started", "date_created")
            if not catalog:
                raise Catalog.DoesNotExist(
                    f"Catalog with short name {catalog_name} does not exist."
                )
            elements = elements.filter(catalog=catalog)
        else: 
            # Two queries isntead of one - can be optimized, but it
            # allows for better exception management
            catalog = Catalog.objects.get(
                short_name=catalog_name,
                version=format_version(catalog_version)
            )
            elements = elements.filter(catalog=catalog)
        return elements
        

class ElementValidationViewset(viewsets.ModelViewSet):
    """Check if the element is valid for 
    the selected or current catalog version"""
    queryset = Element.objects.all().order_by('-date_created')
    serializer_class = ElementSerializer
        
    def retrieve(self, request, *args, **kwargs):
        """Rewriting the default list function"""
        data = loads(request.body)
        in_element = data.get("element", {})
        in_catalog = data.get("catalog", {})
        # Filtering - all elements for the specific catalog
        if in_catalog.get("version") is not None:
            # If catalog version is provided
            res_element = Element.objects.filter(
                catalog__short_name=in_catalog.get("short_name"),
                catalog__version=format_version(in_catalog["version"]),
            )
        else:
            # If latest catalog version
            catalog = Catalog.objects.filter(
                short_name=in_catalog.get("short_name"),
            )
            catalog = catalog.latest("date_started", "date_created")
            res_element = Element.objects.filter(catalog=catalog)
        # Filtering - the element with the required code
        res_element = res_element.get(code=in_element.get("code"))
        # Validating element description - if provided
        if in_element.get("description") == res_element.description \
        or in_element.get("description") is None:
            serializer = self.get_serializer(res_element)
            return Response(serializer.data)
        else:
            raise Element.DoesNotExist


"""Defining the allowed request methods for each ModelViewSet"""
catalogs = CatalogsViewset.as_view({
    "get": "list",
    #"post": "create",  # Uncomment if you want to create catalogs in the API
})
elements = ElementsViewset.as_view({
    "get": "list",
    #"post": "create",  # Uncomment if you want to create elements in the API
})
catalogs_actual = CatalogsActualViewset.as_view({
    "get": "list",
})
elements_by_catalog = ElementsByCatalogViewset.as_view({
    "get": "list",
})
element_validation = ElementValidationViewset.as_view({
    "post": "retrieve",
})