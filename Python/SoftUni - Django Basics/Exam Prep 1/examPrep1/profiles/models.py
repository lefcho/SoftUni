from django.core.validators import MinLengthValidator
from django.db import models

from profiles.validators import AlphaNumericalValidator


class Profile(models.Model):
    username = models.CharField(
        max_length=15,
        validators=[
            MinLengthValidator(2),
            AlphaNumericalValidator(),
        ]

    )

    email = models.EmailField()

    age = models.PositiveIntegerField(
        null=True,
        blank=True,
    )
