from django.db import migrations


def set_price(apps, schema_editor):
    smartphone_model = apps.get_model('main_app', 'Smartphone')

    smartphones = smartphone_model.objects.all()

    for smartphone in smartphones:
        smartphone.price = 120 * len(smartphone.brand)

    smartphone_model.objects.bulk_update(smartphones, ['price'])


def set_category(apps, schema_editor):
    smartphone_model = apps.get_model('main_app', 'Smartphone')

    smartphones = smartphone_model.objects.all()

    for smartphone in smartphones:
        if smartphone.price >= 750:
            smartphone.category = 'Expensive'
        else:
            smartphone.category = 'Cheap'

    smartphone_model.objects.bulk_update(smartphones, ['category'])


def reverse_data_price_category(apps, schema_editor):
    smartphone_model = apps.get_model('main_app', 'Smartphone')

    smartphones = smartphone_model.objects.all()

    for smartphone in smartphones:
        smartphone.price = smartphone_model._meta.get_field('price').default
        smartphone.category = smartphone_model._meta.get_field('category').default

    smartphone_model.objects.bulk_update(smartphones, ['category', 'price'])


def set_data(apps, schema_editor):
    set_price(apps, schema_editor)
    set_category(apps, schema_editor)


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0013_smartphone'),
    ]

    operations = [
        migrations.RunPython(set_data, reverse_data_price_category)
    ]
