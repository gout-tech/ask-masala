# Generated by Django 2.2.1 on 2019-06-10 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_us', '0015_auto_20190610_0809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
