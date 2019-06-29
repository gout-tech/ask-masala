from django.db import models


class Clients(models.Model):

    image = models.ImageField(upload_to = 'media/Person_images', help_text='Upload an image with 200 x 100, size:  2.8 kB (2,783 bytes')
    hov_image = models.ImageField(upload_to = 'media/Person_images', help_text='Upload an image with 200 x 100, size:  2.8 kB (2,783 bytes')
    is_published = models.BooleanField(default=True)



    class Meta:
        verbose_name_plural = "Clients"
