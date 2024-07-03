import os
from typing import List

import django
from django.db.models import When, Value, Case


# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()


from main_app.models import ArtworkGallery, Laptop, LaptopOSChoices, ChessPlayer


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


def bulk_create_chess_players(args: List[ChessPlayer]):
    ChessPlayer.objects.bulk_create(args)


def delete_chess_players():
    ChessPlayer.objects.filter(title='no title').delete()


def change_chess_games_won():
    ChessPlayer.objects.filter(title='GM').update(games_won=30)


def change_chess_games_lost():
    ChessPlayer.objects.filter(title='no title').update(games_lost=25)


def change_chess_games_drawn():
    ChessPlayer.objects.update(games_drawn=10)


def grand_chess_title_GM():
    ChessPlayer.objects.filter(rating__gte=2400).update(title='GM')


def grand_chess_title_IM():
    ChessPlayer.objects.filter(rating__range=(2300, 2399)).update(title='IM')


def grand_chess_title_FM():
    ChessPlayer.objects.filter(rating__range=(2200, 2299)).update(title='FM')


def grand_chess_title_regular_player():
    ChessPlayer.objects.filter(rating__range=(0, 2199)).update(title='regular player')












