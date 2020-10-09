from rest_framework import serializers, pagination
from .models import Catalog, Element


class CatalogSerializer(serializers.ModelSerializer):
    """This class is used to manage how we pass Catalog to the client app."""

    class Meta:
        model = Catalog
        fields = '__all__'


class ElementSerializer(serializers.ModelSerializer):
    """This class is used to manage how we pass Element to the client app."""

    class Meta:
        model = Element
        fields = '__all__'
