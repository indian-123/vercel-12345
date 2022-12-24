from django.db import models

# Create your models here.
class Datas(models.Model):
    Name=models.CharField(max_length=20)
    Password=models.CharField(max_length=20)
    Address=models.CharField(max_length=20)
    Contact=models.IntegerField()
    Mail=models.CharField(max_length=20)
    image=models.ImageField(upload_to="imges/",blank=True, null=True)
#     image=models.ImageField(upload_to="imges/" ,blank=True,null=True)
