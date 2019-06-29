from django.db import models
from django.core.validators import RegexValidator


class ContactUs(models.Model):

    Name = models.CharField(max_length=100)
    Email = models.EmailField(max_length=100)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,10}$',
                                 message="Enter a valid phone number")
    Phone = models.CharField(validators=[phone_regex], max_length=10)  # validators should be a list
    #phone = models.CharField(max_length=10)
    Subject = models.CharField(max_length=100)
    Message = models.CharField(max_length=200)

    def __str__(self):
        return self.Name

    class Meta:
        verbose_name_plural = "Contact Us"



