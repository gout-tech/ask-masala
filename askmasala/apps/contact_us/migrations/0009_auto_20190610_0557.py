# Generated by Django 2.2.1 on 2019-06-10 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_us', '0008_auto_20190610_0550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='phone',
            field=models.IntegerField(),
        ),
    ]
