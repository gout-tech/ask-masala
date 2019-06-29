# Generated by Django 2.2.1 on 2019-05-17 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_us', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=13)),
                ('subject', models.CharField(max_length=100)),
                ('message', models.CharField(max_length=300)),
            ],
        ),
        migrations.AlterField(
            model_name='contactus',
            name='phno',
            field=models.CharField(max_length=13),
        ),
    ]
