from django.db import models

class Products(models.Model):
    product_name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(decimal_places=2,max_digits=10)
    availability = models.BooleanField(default=True)
    category = models.ManyToManyField('Categories')
    exp_date = models.DateTimeField()

    def __str__(self):
        return self.product_name

    class Meta:
        verbose_name_plural = "Products"



def get_image_filename(instance,filename):
    id = instance.product.id
    return "media/product_images/%s.jpg" %(id)


class Images(models.Model):
    product = models.ForeignKey(Products, default=None, on_delete=models.CASCADE,related_name='product_images')
    image = models.ImageField(upload_to=get_image_filename, verbose_name='Image', help_text='Upload an image with 1000 x 667  , size: 40.7 kB (40,749 bytes)')
    default_image = models.BooleanField(default=False)


    class Meta:
        verbose_name_plural = "Images"


class Categories(models.Model):
    category = models.CharField(max_length=200)

    def __str__(self):
        return self.category

    class Meta:
        verbose_name_plural = "Categories"

