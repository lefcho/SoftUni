from django.db import migrations


def set_item_rarity(apps, schema_editor):
    item_model = apps.get_model('main_app', 'Item')

    items = item_model.objects.all()

    for item in items:
        if item.price <= 10:
            item.rarity = 'Rare'
        elif item.price <= 20:
            item.rarity = 'Very rare'
        elif item.price <= 30:
            item.rarity = 'Extremely rare'
        else:
            item.rarity = 'Mega rare'

    item_model.objects.bulk_update(items, ['rarity'])


def set_item_rarity_default(apps, schema_editor):
    item_model = apps.get_model('main_app', 'Item')

    items = item_model.objects.all()

    for item in items:
        item.rarity = item_model._meta.get_field('rarity').default

    item_model.objects.bulk_update(items, ['rarity'])


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0011_item'),
    ]

    operations = [
        migrations.RunPython(set_item_rarity, set_item_rarity_default)
    ]
