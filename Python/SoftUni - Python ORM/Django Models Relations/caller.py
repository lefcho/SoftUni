import os
from datetime import timedelta, date

import django
from django.db.models import QuerySet

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Author, Artist, Song, Product, Review, DrivingLicense, Driver, Owner, Registration, Car


def show_all_authors_with_their_books():
    authors_with_books = []

    authors = Author.objects.all().order_by('id')

    for author in authors:
        books = author.book_set.all()

        if not books:
            continue

        titles = ', '.join(b.title for b in books)
        authors_with_books.append(
            f'{author.name} has written - {titles}!'
        )

    return '\n'.join(authors_with_books)


def delete_all_authors_without_books() -> None:
    Author.objects.filter(book__isnull=True).delete()


def add_song_to_artist(artist_name: str, song_title: str) -> None:
    artist = Artist.objects.get(name=artist_name)
    song = Song.objects.get(title=song_title)

    artist.songs.add(song)


def get_songs_by_artist(artist_name: str) -> QuerySet[Song]:
    return Artist.objects.get(name=artist_name).songs.all().order_by('-id')


def remove_song_from_artist(artist_name: str, song_title: str) -> None:
    artist = Artist.objects.get(name=artist_name)
    song = Song.objects.get(title=song_title)

    artist.songs.remove(song)


def calculate_average_rating_for_product_by_name(product_name: str) -> float:
    product = Product.objects.get(name=product_name)
    reviews = product.reviews.all()

    return sum(r.rating for r in reviews) / len(reviews)


def get_reviews_with_high_ratings(threshold: int) -> QuerySet[Review]:
    return Review.objects.filter(rating__gte=threshold)


def get_products_with_no_reviews() -> QuerySet[Product]:
    return Product.objects.filter(reviews__isnull=True).order_by('-name')


def delete_products_without_reviews() -> None:
    get_products_with_no_reviews().delete()


def calculate_licenses_expiration_dates() -> str:
    licenses = DrivingLicense.objects.all().order_by('-license_number')
    return ('\n'.join
            (f'License with number: {l.license_number} expires on {l.issue_date + timedelta(days=365)}!' for l in licenses))


def get_drivers_with_expired_licenses(due_date: date) -> QuerySet[Driver]:
    min_crate_date = due_date - timedelta(days=365)

    return Driver.objects.filter(
        license__issue_date__gt=min_crate_date
    )


def register_car_by_owner(owner: Owner) -> str:
    registration = Registration.objects.filter(car__isnull=True).first()
    car = Car.objects.filter(registration__isnull=True).first()

    car.owner = owner
    car.save()

    registration.registration_date = date.today()
    registration.car = car
    registration.save()

    return f"Successfully registered {car.model} to {owner.name} with registration number {registration.registration_number}."

































