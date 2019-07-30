from django.db import models

from django.utils import timezone

# Create your models here.
class Oposy(models.Model):
    opo_name = models.CharField('opo_name', max_length=200)
    opo_title = models.CharField('opo_title', max_length=200)
    opo_cat = models.CharField('opo_category', max_length=100)
    opo_cat_name = models.CharField('opo_category_name', max_length=100)
    opo_text = models.TextField('opo_text') # caly html :D
    year_added = models.CharField('year_added', max_length=4)
    def __str__(self):
        return self.opo_name
    def zakalce(self):
        return self.objects.filter(opo_cat='zakalec')
    def okruchy(self):
        return self.objects.filter(opo_cat='okruchy')
    def zarty(self):
        return self.objects.filter(opo_cat='zartem')
    def serio(self):
        return self.objects.filter(opo_cat='serio')
    def najnowsze(self):
        return self.objects.filter(year_added=str(timezone.now().year))

class Emaile(models.Model):
    email = models.EmailField('email_name') # in django all fields are required by default
    created = models.DateTimeField('created_date', default=timezone.now())
    def __str__(self):
        return self.email

# https://docs.djangoproject.com/en/2.2/topics/db/queries/#field-lookups-intro
