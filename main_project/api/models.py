from django.db import models

from django.utils import timezone
# Create your models here.


class User(models.Model):
    
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    
    
    def __str__(self):
        return self.name 
  
  
class Url(models.Model):
    
    title = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.title 
    