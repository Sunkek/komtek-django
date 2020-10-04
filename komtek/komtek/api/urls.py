from django.urls import include, path
from .views import CatalogsViewset, ElementsViewset

urlpatterns = [
    path("catalogs/", CatalogsViewset.as_view({'get': 'list'}), name="catalogs"),
    path("elements/", ElementsViewset.as_view({'get': 'list'}), name="elements"),
]
