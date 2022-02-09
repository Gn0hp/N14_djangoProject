# Generated by Django 3.2.9 on 2021-12-03 02:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0031_remove_product_capacity_product456'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.city')),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.district')),
                ('ward', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.ward')),
            ],
        ),
        migrations.AddField(
            model_name='customer',
            name='address',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.address'),
        ),
    ]
