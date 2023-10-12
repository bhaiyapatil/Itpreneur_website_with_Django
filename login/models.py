from django.db import models

# Create your models here.
        
class Job(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=100)
    summary = models.CharField(max_length=350)
    pdf = models.FileField(upload_to='pdf/')
    
    
    def __str__(self):
        return self.title
    