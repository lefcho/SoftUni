from django.core.validators import MinLengthValidator
from django.db import models
from authors.validators import OnlyLettersValidator, ExactDigitsValidator


class Author(models.Model):
    first_name = models.CharField(
        max_length=40,
        validators=[
            MinLengthValidator(4),
            OnlyLettersValidator(),
        ]
    )

    last_name = models.CharField(
        max_length=50,
        validators=[
            MinLengthValidator(2),
            OnlyLettersValidator(),
        ]
    )

    passcode = models.CharField(
        max_length=6,
        validators=[
            ExactDigitsValidator(6),
        ]
    )

    pets_number = models.PositiveSmallIntegerField()

    info = models.TextField(
        null=True,
        blank=True,
    )

    image_url = models.URLField(
        null=True,
        blank=True,
    )
