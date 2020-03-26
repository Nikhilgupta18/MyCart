from django.db import models


# Create your models here.

class Product(models.Model):
    P_name = models.CharField(max_length=100)
    P_price = models.IntegerField()
    gender = (
        ('M', 'Male'),
        ('F', 'Female'),

    )
    P_gender = models.CharField(max_length=5, choices=gender, blank=True)
    sizes = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    category = (
        ('C', 'Clothing'),
        ('E', 'Electronics'),
        ('S', 'Sports'),
        ('Ed', 'Education'),
    )
    P_category = models.CharField(max_length=20, choices=category)
    P_sizes = models.CharField(max_length=10, choices = sizes, blank=True)
    P_desc = models.TextField()
    P_image = models.ImageField(upload_to='product_images/', blank=True)

    def __str__(self):
        return self.P_name




class News(models.Model):
    title = models.CharField(max_length=256)
    text = models.TextField(max_length=500)



