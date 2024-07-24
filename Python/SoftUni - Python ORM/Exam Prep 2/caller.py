import os
import django
from django.db.models import Q, Count, F, Case, When, Value, BooleanField

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import Profile, Product, Order


def get_profiles(search_string=None):
    if search_string is None:
        return ''

    profiles = Profile.objects.filter(
        Q(full_name__icontains=search_string)
        |
        Q(email__icontains=search_string)
        |
        Q(phone_number__icontains=search_string)
    ).order_by('full_name')

    if not profiles.exists():
        return ''

    return "\n".join(
        f"Profile: {p.full_name}, email: {p.email}, phone number: {p.phone_number}, orders: {p.orders.count()}"
        for p in profiles
    )


def get_loyal_profiles():
    profiles = Profile.objects.get_regular_customers()

    if not profiles:
        return ''

    return '\n'.join(f'Profile: {p.full_name}, orders: {p.orders_count}' for p in profiles)


def get_last_sold_products():
    last_order = Order.objects.prefetch_related('products').last()

    if last_order is None or not last_order.products.exists():
        return ''

    products = ', '.join(last_order.products.order_by('name').values_list('name', flat=True))

    return f'Last sold products: {products}'


def get_top_products():
    products = (Product.objects
                .annotate(orders_count=Count('orders'))
                .filter(orders_count__gt=0)
                .order_by('-orders_count', 'name'))[:5]

    if not products.exists():
        return ''

    product_line = '\n'.join(f'{p.name}, sold {p.orders_count} times' for p in products)

    return 'Top products:\n' + product_line


def apply_discounts():
    num_of_updates = (Order.objects
                      .annotate(products_count=Count('products'))
                      .filter(products_count__gt=2, is_completed=False)
                      .update(total_price=F('total_price') * 0.9))

    return f"Discount applied to {num_of_updates} orders."


def complete_order():
    order = Order.objects.filter(is_completed=False).first()

    if not order:
        return ''

    order.products.all().update(
        in_stock=F('in_stock') - 1,
        is_available=Case(
            When(in_stock=1, then=Value(False)),
            default=F('is_available'),
            output_field=BooleanField()
        )
    )

    order.is_completed = True
    order.save()

    return "Order has been completed!"































