# Generated by Django 3.2.9 on 2021-11-30 10:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0024_product_img_color_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product_img_color',
            name='productID',
        ),
    ]
