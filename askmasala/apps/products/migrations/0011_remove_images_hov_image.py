from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_auto_20190617_0519'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='images',
            name='hov_image',
        ),
    ]
