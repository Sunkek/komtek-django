from random import choice, randint
from django.contrib import admin, messages
from .models import Catalog, Element
from .utils import format_version

LETTERS = list("qwertyuiopasdfghjklzxcvbnm")

@admin.register(Catalog)
class CatalogAdmin(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):
        """Overriding Catalog's save model function to format its version"""
        obj.version = format_version(obj.version)
        super().save_model(request, obj, form, change)

    def populate(self, request, queryset):
        for catalog in queryset:
            try:
                for i in range(10):
                    element = Element(
                        catalog=catalog,
                        code=f"{randint(0,9)}{choice(LETTERS)}{choice(LETTERS)}",
                        description="Автоматически сгенерированный элемент",
                    )
                    element.save()
            except Exception as e:
                print(e)
        self.message_user(
            request, 
            "Элементы добавлены", 
            messages.SUCCESS
        )
    populate.short_description = "Добавить 10 случайных элементов"


admin.site.register(Element)