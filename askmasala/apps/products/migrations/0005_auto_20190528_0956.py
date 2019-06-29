# Generated by Django 2.2.1 on 2019-05-28 09:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20190521_0824'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='images',
            name='product',
        ),
        migrations.AddField(
            model_name='products',
            name='images',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='products.Images'),
        ),
    ]
