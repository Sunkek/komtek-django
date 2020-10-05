from django.urls import include, path
from .views import catalogs, catalogs_actual, elements

urlpatterns = [
    path("catalogs/", catalogs, name="catalogs"),
    path("catalogs/actual/<str:date>/", catalogs_actual, name="catalogs_actual"),
    path("catalogs/actual/", catalogs_actual, name="catalogs_actual"),
    path("elements/", elements, name="elements"),
]
