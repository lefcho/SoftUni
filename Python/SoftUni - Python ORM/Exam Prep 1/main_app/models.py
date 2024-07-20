from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator
from django.db import models
from main_app.mixins import AwardedMixin, LastUpdatedMixin


class BaseModel(models.Model):
    class Meta:
        abstract = True

    full_name = models.CharField(
        max_length=120,
        validators=[MinLengthValidator(2)],
    )

    birth_date = models.DateField(
        default='1900-01-01',
    )

    nationality = models.CharField(
        max_length=50,
        default='Unknown',
    )


class Director(BaseModel):
    years_of_experience = models.SmallIntegerField(
        validators=[MinValueValidator(0)],
        default=0,
    )


class Actor(BaseModel, AwardedMixin, LastUpdatedMixin):
    pass


class Movie(AwardedMixin, LastUpdatedMixin):
    class GenreChoices(models.TextChoices):
        ACTION = 'Action', 'Action'
        COMEDY = 'Comedy', 'Comedy'
        DRAMA = 'Drama', 'Drama'
        OTHER = 'Other', 'Other'

    title = models.CharField(
        max_length=150,
        validators=[MinLengthValidator(5)],
    )

    release_date = models.DateField()

    storyline = models.TextField(
        null=True,
        blank=True,
    )

    genre = models.CharField(
        max_length=10,
        choices=GenreChoices.choices,
        validators=[MinLengthValidator(6)],
        default='Other',
    )

    rating = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        validators=[MinValueValidator(0.0), MaxValueValidator(10.0)],
        default=0.0,
    )

    is_classic = models.BooleanField(
        default=False,
    )

    director = models.ForeignKey(
        to=Director,
        on_delete=models.CASCADE,
        related_name='movies_directed',
    )

    starring_actor = models.ForeignKey(
        to=Actor,
        null=True,
        on_delete=models.SET_NULL,
        related_name='starred_movies',
    )

    actors = models.ManyToManyField(
        to=Actor,
        related_name='movies',
    )








































