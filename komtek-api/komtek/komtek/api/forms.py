
from django.contrib.admin.helpers import ActionForm
from django.core.validators import MaxValueValidator, MinValueValidator
from django import forms


class AmountForm(ActionForm):
    amount = forms.IntegerField(
        required=False,
        label="Количество: ",
        initial=10,
        validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ]
    )
