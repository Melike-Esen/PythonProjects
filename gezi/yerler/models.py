from django.db import models

class Yer(models.Model):
    adi=models.CharField(max_length=50)
    tarih=models.DateField(null=True)
    yazar=models.CharField(max_length=50,null=True)
