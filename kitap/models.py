from django.db import models

class Book(models.Model):
    adi=models.CharField(max_length=50)
    yazari=models.CharField(max_length=200)
    konusu=models.CharField(max_length=30)
