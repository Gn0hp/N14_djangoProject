# Generated by Django 3.2.9 on 2021-11-30 14:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0029_rename_product_product_capacity_product456'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product_capacity',
            old_name='product123',
            new_name='product',
        ),
    ]
