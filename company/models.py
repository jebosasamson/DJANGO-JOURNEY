from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=20)
    type = models.CharField(max_length=20)

class News(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    author = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='uploads', blank=True, null=True)

    def __str__(self):
        return self.title
    

class Programs(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()   
    image = models.ImageField(upload_to='uploads', blank=True, null=True)

    def __str__(self):
        return self.title

class Exercise(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField( ) 
    image = models.ImageField(upload_to='uploads', blank=True, null=True)   

    def __str__(self):
        return self.title
    
class OurClub(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()   
    image = models.ImageField(upload_to='uploads', blank=True, null=True)

    def __str__(self):
        return self.title
class Testimonial(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()   
    image = models.ImageField(upload_to='uploads', blank=True, null=True)
    
    def __str__(self):
        return self.title
    
class SocialIcons(models.Model):
    title = models.CharField(max_length=20)  
    image = models.ImageField(upload_to='uploads', blank=True, null=True)
    
    def __str__(self):
        return self.title
class About(models.Model):
    description = models.TextField() 

    def __str__(self):
        return self.description
class ContactInfo(models.Model):
    address = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.address

