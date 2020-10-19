from random import choice, randint
from datetime import date as dt_date

from django.contrib import admin, messages
from django.contrib.admin.helpers import ActionForm
from django import forms
from django.db.utils import IntegrityError

from .models import Catalog, Element
from .utils import format_version

LETTERS = list("QWERTYUIOPASDFGHJKLZXCVBNM")


class NumberOfElementsForm(ActionForm):
    number = forms.IntegerField(
        required=True,
        label="Количество: ",
        initial=10,
    )


@admin.register(Catalog)
class CatalogAdmin(admin.ModelAdmin):
    actions = ["populate"]

    def save_model(self, request, obj, form, change):
        """Overriding Catalog's save model function to format its version"""
        obj.version = format_version(obj.version)
        super().save_model(request, obj, form, change)

    def populate(self, request, queryset):
        """Add 10 randomly created elements to the selected catalogs.
        If an element already exists - update its creation date."""
        form = NumberOfElementsForm(request.POST)
        for catalog in queryset:
            for i in range(form.cleaned_data["number"]):
                code = f"{randint(0,9)}{choice(LETTERS)}{choice(LETTERS)}"
                element = Element(
                    catalog=catalog,
                    code=code,
                    description="Автоматически сгенерированный элемент",
                )
                try:
                    element.save()
                except IntegrityError:
                    element = Element.objects.get(
                        catalog=catalog,
                        code=code,
                        description="Автоматически сгенерированный элемент",
                    )
                    element.date_created = dt_date.today()
                    element.save()
        self.message_user(
            request, 
            "Элементы добавлены", 
            messages.SUCCESS
        )
    populate.short_description = "Добавить N случайных элементов"


admin.site.register(Element)