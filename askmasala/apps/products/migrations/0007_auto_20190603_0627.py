# Generated by Django 2.2.1 on 2019-06-03 06:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20190528_1000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='product',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='product_images', to='products.Products'),
        ),
    ]
