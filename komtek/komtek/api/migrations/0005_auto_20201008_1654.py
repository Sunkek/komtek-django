# Generated by Django 3.1.2 on 2020-10-08 11:54

from django.db import migrations, models
import komtek.api.models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20201006_1730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalog',
            name='version',
            field=models.CharField(max_length=10, validators=[komtek.api.models.validate_version], verbose_name='Версия'),
        ),
    ]
