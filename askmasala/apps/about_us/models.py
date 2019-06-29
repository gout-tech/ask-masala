from django.db import models


class About(models.Model):

    image = models.ImageField(upload_to = 'media/About_images', help_text='Upload an image with 170 x 160, size:  7.2 kB (7,205 bytes')
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "about"
