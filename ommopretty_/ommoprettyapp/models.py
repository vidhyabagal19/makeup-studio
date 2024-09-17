from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Product(models.Model):
    CAT=((1,"Bridal"),(2,"Fashion"))
    name=models.CharField(max_length=30,verbose_name="makeup_type")
    price=models.FloatField()
    detail=models.CharField(max_length=100,verbose_name="makeup_Detail")
    cat=models.IntegerField(verbose_name="Category",choices=CAT)
    is_active=models.BooleanField(default=True)
    pimage=models.ImageField(upload_to='image')




    def __str__(self):
        return self.name


