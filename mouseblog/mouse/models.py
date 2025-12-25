from django.db import models
from django.contrib.auth.models import User

class Mouse(models.Model):
    marka = models.CharField(max_length=35)
    aydinlatma = models.CharField(max_length=10)
    kul_amac = models.CharField(max_length=10)
    dpi = models.CharField(max_length=35)
    yorum = models.TextField()
    author=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.marka + ' | ' + str(self.author)

