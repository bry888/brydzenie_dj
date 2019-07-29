from django.db import models

from django.utils import timezone

# Create your models here.
class Emaile(models.Model):
    email = models.EmailField('email_name') # in django all fields are required by default
    created = models.DateTimeField('created_date', default=timezone.now())
    def __str__(self):
        return self.email
