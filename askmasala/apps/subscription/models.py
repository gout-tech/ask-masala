from django.db import models

class Subscribers(models.Model):

    email = models.EmailField(max_length=100)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.email
