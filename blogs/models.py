from django.db import models

# Create your models here.


class Blogs(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    image = models.ImageField(upload_to='image/')
    body = models.CharField(max_length=2000)
    
    def summary(self):
        return self.body[0:100]
    
    
    def __str__(self):
        return self.title
    
    
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.IntegerField()
    desc = models.TextField()
    
    def __str__(self):
        return self.name
    
    
    