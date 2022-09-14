from django.db import models
from django.db.models.fields import CharField, URLField

from django.db.models.fields.files import ImageField 

 


# Create your models here.
class project(models.Model):
    title = CharField(max_length=100)
    descripcion = CharField(max_length = 150)
    image =ImageField(upload_to='miportafolio/images/')
    url = URLField(blank=True)
    