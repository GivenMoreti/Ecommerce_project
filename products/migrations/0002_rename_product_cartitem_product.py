# Generated by Django 4.2.2 on 2023-06-14 17:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="cartitem",
            old_name="Product",
            new_name="product",
        ),
    ]
