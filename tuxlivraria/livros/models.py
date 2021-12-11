from django.db import models
from django.utils import timezone

# Create your models here.

class Categoria(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Livros(models.Model):
   title = models.CharField(max_length=40)
   author = models.CharField(max_length=40)
   isbn = models.CharField(max_length=40)
   publishingCompany = models.CharField(max_length=40)
   publicationDate = models.DateField(default=timezone.now)
   description = models.TextField(blank=True)
   categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)



class Livros2(models.Model):
    title = models.CharField(max_length=40)
    img = models.CharField(max_length=250)
    author = models.CharField(max_length=40)
    isbn = models.CharField(max_length=40)
    publishingCompany = models.CharField(max_length=40)
    publicationDate = models.DateField(default=timezone.now)
    description = models.TextField(blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.title

