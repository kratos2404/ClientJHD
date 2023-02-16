from django.db import models

# Create your models here.
class Contact(models.Model):
     sno= models.AutoField(primary_key=True)
     name= models.CharField(max_length=255)
     phone= models.IntegerField()
     email= models.CharField(max_length=100)
     address = models.CharField(max_length=500, null=True)
     map_requirements= models.TextField()
     plot_size = models.IntegerField(blank=True, null=True)
     road_direction = models.CharField(max_length=50, blank=True, null=True)
     timeStamp=models.DateTimeField(auto_now_add=True, blank=True)
     def __str__(self):
          return "Message from " + self.name + ' - ' + self.email


class VastuMaps(models.Model):
    image = models.ImageField(upload_to='blog', height_field=None, width_field=None, max_length=None)
    slug = models.SlugField(max_length=100, unique=True)
    

class Design(models.Model):
    image = models.ImageField(upload_to='design')
    slug = models.SlugField(max_length=100, unique=True)

class Search(models.Model):
    address = models.CharField(max_length=250, null=True)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.address