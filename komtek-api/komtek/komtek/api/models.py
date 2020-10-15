from django.db import models
from django.core.exceptions import ValidationError
import uuid

VERSION_SYMBOLS = list("1234567890.")

def validate_version(value):
    """Check the version format before saving the catalog to the database"""
    for symbol in value:
        if symbol not in VERSION_SYMBOLS or value.count(".") > 3:
            raise ValidationError(
                "Некорректный формат версии. Пример корректных форматов: `1.0`, `2`, `3.0.1`, `4.10.10`.",
                params={"value": value},
            )
    

class Catalog(models.Model):
    """Catalog model description with all the required fields"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    short_name = models.CharField("Короткое название", max_length=50)
    full_name = models.CharField("Полное название", max_length=200)
    description = models.CharField("Описание",max_length=1000)
    version = models.CharField(
        "Версия", max_length=10, blank=False, 
        null=False, validators=[validate_version]
    )
    date_created = models.DateField("Дата создания", auto_now_add=True)
    date_started = models.DateField("Дата начала", blank=True, null=True)
    date_expired = models.DateField("Дата окончания", blank=True, null=True)
    
    def __str__(self):
        return f"{self.short_name} {self.version}"

    # Catalogs should have unique versions
    class Meta:
        unique_together = ("short_name", "version")
        verbose_name = "Справочник"
        verbose_name_plural = "Справочники"


class Element(models.Model):
    """An element of a catalog"""
    id = models.AutoField(primary_key=True)
    catalog = models.ForeignKey(
        "Catalog", 
        on_delete=models.CASCADE,
        related_name="elements", 
        verbose_name="Каталог"
    )
    code = models.CharField("Код", max_length=50, blank=False, null=False)
    description = models.CharField("Описание", max_length=500, blank=False, null=False)
    date_created = models.DateField("Дата создания", auto_now_add=True)
    
    def __str__(self):
        dots = "..." if len(self.description) > 10 else ""
        return f"{self.code} {self.description[:10]}{dots}"
    
    # Only one code can be present in a catalog
    class Meta:
        unique_together = ("catalog", "code")
        verbose_name = "Элемент"
        verbose_name_plural = "Элементы"
