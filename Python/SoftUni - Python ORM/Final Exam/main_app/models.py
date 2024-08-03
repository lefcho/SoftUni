from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models
from main_app.managers import AstronautManager
from main_app.validators import DigitOnlyValidator


class UpdatedAtMixin(models.Model):
    class Meta:
        abstract = True

    updated_at = models.DateTimeField(auto_now=True)


class Astronaut(UpdatedAtMixin):
    name = models.CharField(
        max_length=120,
        validators=[MinLengthValidator(2)],
    )

    phone_number = models.CharField(
        max_length=15,
        unique=True,
        validators=[DigitOnlyValidator("Only digits allowed")],
    )

    is_active = models.BooleanField(
        default=True,
    )

    date_of_birth = models.DateField(
        null=True,
        blank=True,
    )

    spacewalks = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0)],
    )

    objects = AstronautManager()


class Spacecraft(UpdatedAtMixin):
    name = models.CharField(
        max_length=120,
        validators=[MinLengthValidator(2)],
    )

    manufacturer = models.CharField(
        max_length=100,
    )

    capacity = models.PositiveSmallIntegerField()

    weight = models.FloatField(
        validators=[MinValueValidator(0.0)]
    )

    launch_date = models.DateField()


class Mission(UpdatedAtMixin):

    class StatusChoices(models.TextChoices):
        PLANNED = 'Planned', 'Planned'
        ONGOING = 'Ongoing', 'Ongoing'
        COMPLETED = 'Completed', 'Completed'

    name = models.CharField(
        max_length=120,
        validators=[MinLengthValidator(2)],
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    status = models.CharField(
        max_length=9,
        default='Planned',
        choices=StatusChoices.choices
    )

    launch_date = models.DateField()

    spacecraft = models.ForeignKey(
        to=Spacecraft,
        on_delete=models.CASCADE,
        related_name='missions'
    )

    astronauts = models.ManyToManyField(
        to=Astronaut,
        related_name='missions',
    )

    commander = models.ForeignKey(
        to=Astronaut,
        null=True,
        on_delete=models.SET_NULL,
        related_name='commander_missions'
    )







