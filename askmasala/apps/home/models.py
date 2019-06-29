from django.db import models

# Create your models here.


def get_image_filename(instance, filename):
    return '/'.join(['images', str(instance.name), filename])


class Images(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to=get_image_filename, verbose_name='Image', help_text='Upload an image with 1920 x 920 , size: 58.8 kB (58,821 bytes) ')

    class Meta:
        verbose_name_plural = "Images"


