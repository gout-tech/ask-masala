from django.db import models

# Create your models here.
from django.db import models

# Create your models here.


def get_image_filename(instance, filename):
    return '/'.join(['images', str(instance.imgname), filename])


class Testimonial(models.Model):
    imgname = models.CharField(max_length=100)
    image = models.ImageField(upload_to=get_image_filename, verbose_name='Image', help_text='Upload an image with 320 X 300 , size: 15.9 kB (15,856 bytes)')
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    jobs = models.CharField(max_length=100)
    is_published = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Testimonials"