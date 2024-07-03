import os
import django

from main_app.models import ArtworkGallery

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

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