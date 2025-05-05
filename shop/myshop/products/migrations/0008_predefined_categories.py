from django.db import migrations

def create_predefined_categories(apps, schema_editor):
    Category = apps.get_model('products', 'Category')
    predefined_categories = [
        'Road Bikes',
        'Gravel Bikes',
        'E-Bikes',
        'Mountain Bikes',
        'Accessories',
        'Clothing',
        'Bike Parts',
    ]
    for category_name in predefined_categories:
        Category.objects.create(name=category_name)

class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_alter_product_category'),
    ]

    operations = [
        migrations.RunPython(create_predefined_categories),
    ]
