# Generated by Django 2.2.1 on 2019-06-10 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0003_auto_20190610_1136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clients',
            name='hov_image',
            field=models.ImageField(help_text='Upload an image with 200 x 100, size:  2.8 kB (2,783 bytes', upload_to='media/Person_images'),
        ),
    ]
