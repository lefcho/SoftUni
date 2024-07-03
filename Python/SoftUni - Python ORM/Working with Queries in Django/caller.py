import os
from typing import List

import django
from django.db.models import When, Value, Case


# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()


from main_app.models import ArtworkGallery, Laptop, LaptopOSChoices
# Import your models
# Create and check models
# Run and print your queries


def show_highest_rated_art():
    best_art = ArtworkGallery.objects.order_by('-rating', 'id').first()

    return f"{best_art.art_name} is the highest-rated art with a {best_art.rating} rating!"


def bulk_create_arts(first_art: ArtworkGallery, second_art: ArtworkGallery):
    new_artworks = [first_art, second_art]
    ArtworkGallery.objects.bulk_create(new_artworks)


def delete_negative_rated_arts():
    ArtworkGallery.objects.filter(rating__lt=0).delete()


def show_the_most_expensive_laptop():
    expensive_laptop = Laptop.objects.order_by('-price', '-id').first()

    return f"{expensive_laptop.brand} is the most expensive laptop available for {expensive_laptop.price}$!"


def bulk_create_laptops(args: List[Laptop]):
    Laptop.objects.bulk_create(args)


def update_to_512_GB_storage():
    Laptop.objects.filter(brand__in=('Asus', 'Lenovo')).update(storage=512)


def update_to_16_GB_memory():
    Laptop.objects.filter(brand__in=('Apple', 'Dell', 'Acer')).update(memory=16)


def update_operation_systems():
    Laptop.objects.update(
        operation_system=Case(
            When(brand='Asus', then=Value(LaptopOSChoices.WINDOWS)),
            When(brand='Apple', then=Value(LaptopOSChoices.MACOS)),
            When(brand__in=('Dell', 'Acer'), then=Value(LaptopOSChoices.LINUX)),
            When(brand='Lenovo', then=Value(LaptopOSChoices.CHROME_OS))
        )
    )


def delete_inexpensive_laptops():
    Laptop.objects.filter(price__lt=1200).delete()













