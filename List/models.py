from django.db import models

# Create your models here.
class UserList(models.Model):
    item=models.CharField(max_length=60)
    quantity=models.IntegerField(null=True,blank=True,default=1)
    check=models.BooleanField(default=False,null=True,blank=True)