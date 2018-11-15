from django.db import models

class User(models.Model):
     First_name=models.CharField(max_length=264,unique=True)
     Last_Name=models.CharField(max_length=264,unique=True)
     Email=models.CharField(max_length=264,unique=True)


