from django.urls import include, path
from .views import catalogs, catalogs_actual, elements, elements_by_catalog

urlpatterns = [
    path("catalogs/actual/<str:date>/", catalogs_actual, name="catalogs_actual"),
    path("catalogs/actual/", catalogs_actual, name="catalogs_actual"),

    path("elements/from/", elements_by_catalog, name="elements_by_catalog"),

    path("catalogs/", catalogs, name="catalogs"),
    path("elements/", elements, name="elements"),
]
