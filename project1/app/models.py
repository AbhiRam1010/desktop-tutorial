from django.db import models

# Create your models here.


class School(models.Model):
    name=models.CharField( max_length=50)
    password=models.CharField( max_length=50)
    user_name=models.CharField(primary_key=True, max_length=50)
    
    def __str__(self) :
        return self.name