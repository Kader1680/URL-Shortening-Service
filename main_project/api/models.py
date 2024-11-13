from django.db import models

from django.utils import timezone
# Create your models here.


# class User(models.Model):
    
#     username = models.CharField(max_length=255, default='default_username')
#     email = models.CharField(max_length=255, default='default_email')
#     passowrd = models.CharField(max_length=255, default='default_password')


#     def __str__(self):
#         return self.username    
  
  
class Url(models.Model):
    
    title = models.TextField()
    slug = models.CharField(max_length=15)
    date = models.DateTimeField(default=timezone.now)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return  {self.title} 
    