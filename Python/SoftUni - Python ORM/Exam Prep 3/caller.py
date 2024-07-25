import os
import django
from django.db.models import Q, Count

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import Author, Article, Review


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

    if top_author is None or not top_author.reviews_count:
        return ''

    return f'Top Reviewer: {top_author.full_name} with {top_author.reviews_count} published reviews.'



















