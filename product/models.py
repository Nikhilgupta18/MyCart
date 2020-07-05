from django.db import models
from django.db.models.signals import pre_save, post_save, m2m_changed


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

    P_name = models.CharField(max_length=250)
    P_price = models.IntegerField()  # MRP of the product(original price)
    P_gender = models.CharField(max_length=5, choices=gender, blank=True)
    P_category = models.CharField(max_length=20, choices=category)
    P_sizes = models.CharField(max_length=10, choices=sizes, blank=True)
    P_desc = models.TextField()
    P_image = models.ImageField(upload_to='product_images/', blank=True)
    disc_price = models.IntegerField(blank=True, null=True)  # SP selling price of the product
    P_disc = models.IntegerField(blank=True, null=True)  # discount % if any
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.P_name


def pre_save_product_receiver(sender, instance, *args, **kargs):
    if 0 < instance.disc_price < instance.P_price:
        disc = (instance.P_price - instance.disc_price) / instance.P_price
        instance.P_disc = disc * 100
    else:
        instance.disc_price = instance.P_price
        instance.P_disc = 0


pre_save.connect(pre_save_product_receiver, sender=Product)
