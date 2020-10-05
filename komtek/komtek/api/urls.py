from django.urls import include, path
from .views import catalogs, elements

urlpatterns = [
    path("catalogs/", catalogs, name="catalogs"),
    path("elements/", elements, name="elements"),
]
