from django.db import models

class User(models.Model):
    name = models.CharField(max_length=200)
    birth_date = models.DateField('Birth Date')

    def __str__(self):
        return self.name  

class Log(models.Model):
    date =  models.DateTimeField()
    content = models.CharField(max_length=200)
    user =  models.ForeignKey('User',on_delete=models.CASCADE,)

    def __str__(self):
        return self.content

# Create your models here.
