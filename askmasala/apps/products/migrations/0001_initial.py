# Generated by Django 2.2.1 on 2019-05-16 11:18

import apps.products.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('availability', models.CharField(max_length=100)),
                ('exp_date', models.DateTimeField()),
                ('category', models.ManyToManyField(to='products.Categories')),
            ],
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=apps.products.models.get_image_filename, verbose_name='Image')),
                ('product', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='products.Products')),
            ],
        ),
    ]
