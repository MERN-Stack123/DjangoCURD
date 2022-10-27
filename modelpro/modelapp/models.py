from django.db import models

class Emp(models.Model):
    eno=models.IntegerField()
    ename=models.CharField(max_length=100)
    eloc=models.CharField(max_length=50)
    email=models.EmailField()

    
def __str__(self):
    return self.name

