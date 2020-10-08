from django.contrib import admin
from .models import Catalog, Element
from .utils import format_version

@admin.register(Catalog)
class CatalogAdmin(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):
        obj.version = format_version(obj.version)
        super().save_model(request, obj, form, change)


admin.site.register(Element)