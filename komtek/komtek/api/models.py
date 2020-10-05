from django.db import models

class Catalog(models.Model):
    """Catalog model description with all the required fields"""
    short_name = models.CharField(max_length=50)
    full_name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    version = models.CharField(max_length=10, blank=False, null=False)
    date_created = models.DateField(auto_now_add=True)
    date_released = models.DateField(blank=True, null=True)
    date_expired = models.DateField(blank=True, null=True)
    
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
    code = models.CharField(max_length=50, blank=False, null=False)
    value = models.CharField(max_length=500, blank=False, null=False)
    date_created = models.DateField(auto_now_add=True)