# Generated by Django 5.0.7 on 2025-04-21 11:51

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0011_product_autor"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="pdf",
        ),
    ]
