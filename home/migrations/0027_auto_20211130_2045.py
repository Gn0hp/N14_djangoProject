# Generated by Django 3.2.9 on 2021-11-30 13:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0026_rename_product_product_img_color_productid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product_capacity',
            old_name='productID',
            new_name='product',
        ),
        migrations.RenameField(
            model_name='product_img_color',
            old_name='productID',
            new_name='product',
        ),
    ]
