import os
import django
from django.db.models import Q, Count, Avg

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import Author, Article


def get_authors(search_name=None, search_email=None):
    if search_name is None and search_email is None:
        return ''

    name_query = Q(full_name__icontains=search_name)
    email_query = Q(email__icontains=search_email)

    if search_name is not None and search_email is not None:
        query = Q(name_query & email_query)
    elif search_name is not None:
        query = name_query
    else:
        query = email_query

    authors = Author.objects.filter(query).order_by('-full_name')

    if not authors:
        return ''

    return '\n'.join(f'Author: {a.full_name}, email: {a.email}, status: '
                     f'{"Banned" if a.is_banned else "Not Banned"}' for a in authors)


def get_top_publisher():
    top_author = Author.objects.get_authors_by_article_count().first()

    if top_author is None or not top_author.articles_count:
        return ''

    return f'Top Author: {top_author.full_name} with {top_author.articles_count} published articles.'


def get_top_reviewer():
    top_author = (Author.objects
                  .annotate(reviews_count=Count('reviews'))
                  .order_by('-reviews_count', 'email')
                  .first())

    if top_author is None or top_author.reviews_count == 0:
        return ''

    return f'Top Reviewer: {top_author.full_name} with {top_author.reviews_count} published reviews.'


def get_latest_article():
    last_article = (Article.objects
                    .prefetch_related('authors', 'reviews')
                    .annotate(average_rating=Avg('reviews__rating'))
                    .order_by('-published_on')
                    .first()
    )

    if last_article is None:
        return ''

    authors = ', '.join(a.full_name for a in last_article.authors.all().order_by('full_name'))
    num_reviews = last_article.reviews.count()
    average_rating = last_article.average_rating or 0.0

    return (f"The latest article is: {last_article.title}. Authors: {authors}. "
            f"Reviewed: {num_reviews} times. Average Rating: {average_rating:.2f}.")


def get_top_rated_article():
    top_article = (Article.objects
                   .annotate(average_rating=Avg('reviews__rating'))
                   .order_by('-average_rating', 'title')
                   .first()
    )

    if top_article is None or not top_article.reviews.count():
        return ''

    return (f'The top-rated article is: {top_article.title}, with an average rating of {top_article.average_rating:.2f},'
            f' reviewed {top_article.reviews.count()} times.')


def ban_author(email=None):
    author_to_ban = Author.objects.filter(email__exact=email).first()
    if email is None or author_to_ban is None:
        return "No authors banned."

    author_to_ban.is_banned = True
    author_to_ban.save()
    num_of_deleted_reviews, _ = author_to_ban.reviews.all().delete()

    return f'Author: {author_to_ban.full_name} is banned! {num_of_deleted_reviews} reviews deleted.'
