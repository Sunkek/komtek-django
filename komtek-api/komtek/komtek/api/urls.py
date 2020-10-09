from django.contrib import admin
from django.urls import include, path

import komtek.api.views as v

urlpatterns = [
    path('admin/', admin.site.urls),

    path("catalogs/actual/<str:date>/", v.catalogs_actual, name="catalogs_actual"),
    path("catalogs/actual/", v.catalogs_actual, name="catalogs_actual"),

    path("elements/from/", v.elements_by_catalog, name="elements_by_catalog"),
    path("element/validation/", v.element_validation, name="element_validation"),

    path("catalogs/", v.catalogs, name="catalogs"),
    path("elements/", v.elements, name="elements"),
]
