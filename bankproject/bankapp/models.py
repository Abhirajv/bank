from django.db import models
# Create your models here

class Bank(models.Model):
    username=models.CharField(max_length=250)

    name=models.CharField(max_length=250)

    def __str__(self):
        return self.name
