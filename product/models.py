from django.db import models


# Create your models here.

class Product(models.Model):
    gender = (
        ('M', 'Male'),
        ('F', 'Female'),

    )
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
    offer = (
        ('N', 'New'),
        ('M', 'Medium'),
        ('O', 'Old'),
    )

    P_name = models.CharField(max_length=100)
    P_price = models.IntegerField()
    P_gender = models.CharField(max_length=5, choices=gender, blank=True)
    P_category = models.CharField(max_length=20, choices=category)
    P_sizes = models.CharField(max_length=10, choices=sizes, blank=True)
    P_desc = models.TextField()
    P_image = models.ImageField(upload_to='product_images/', blank=True)
    disc_price = models.IntegerField(blank=True, null=True)
    P_offer = models.CharField(max_length=10, choices=offer, default='New')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.P_name
