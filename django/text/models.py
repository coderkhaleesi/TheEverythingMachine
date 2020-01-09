
from django.db import models


# Create your models here.

class HousingData(models.Model):
    crim = models.IntegerField()
    zn = models.IntegerField()
    indus = models.IntegerField()
    chas = models.IntegerField()
    nox = models.IntegerField()
    rm = models.IntegerField()
    age = models.IntegerField()
    dis = models.IntegerField()
    rad = models.IntegerField()
    tax = models.IntegerField()
    ptratio = models.IntegerField()
    bk = models.IntegerField()
    lstat = models.IntegerField()
#    medv = models.IntegerField()