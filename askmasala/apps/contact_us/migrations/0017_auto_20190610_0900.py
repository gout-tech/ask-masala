# Generated by Django 2.2.1 on 2019-06-10 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_us', '0016_auto_20190610_0817'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='email',
            field=models.CharField(max_length=100),
        ),
    ]
