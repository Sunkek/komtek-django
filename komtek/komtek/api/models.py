from django.db import models

class Catalog(models.Model):
    """Catalog model description with all the required fields"""
    id = models.AutoField(primary_key=True)
    short_name = models.CharField("Короткое название", max_length=50)
    full_name = models.CharField("Полное название", max_length=200)
    description = models.CharField("Описание",max_length=1000)
    version = models.CharField("Версия", max_length=10, blank=False, null=False)
    date_created = models.DateField("Дата создания", auto_now_add=True)
    date_started = models.DateField("Дата начала", blank=True, null=True)
    date_expired = models.DateField("Дата окончания", blank=True, null=True)
    
    def __str__(self):
        return f"{self.short_name} {self.version}"

    # Catalogs should have unique versions
    class Meta:
        unique_together = ("short_name", "version")

class Element(models.Model):
    """An element of a catalog"""
    id = models.AutoField(primary_key=True)
    catalog = models.ForeignKey(
        "Catalog", 
        on_delete=models.CASCADE,
        related_name="elements", 
    )
    code = models.CharField("Код", max_length=50, blank=False, null=False)
    description = models.CharField("Описание", max_length=500, blank=False, null=False)
    date_created = models.DateField("Дата создания", auto_now_add=True)
    
    # Only one code can be present in a catalog
    class Meta:
        unique_together = ("catalog", "code")