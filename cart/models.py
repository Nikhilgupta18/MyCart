from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save, post_save, m2m_changed
from product.models import Product


# from django.contrib.sessions.models import Session


# Create your models here.
# class CartManager(models.Manager):
#     def new_or_get(self, request):
#         print(request.session.get('cart_id'))
#         cart_id = request.session.get('cart_id', None)
#         qs = self.get_queryset().filter(id=cart_id)
#         print(qs)
#         if qs.count() == 1:
#             new_obj = False
#             print('already there')
#             print(request.user)
#             cart_obj = qs.first()
#             if request.user.is_authenticated and cart_obj.user is None:
#                 cart_obj.user = request.user
#                 cart_obj.save()
#
#         else:  # if it does not exists
#             new_obj = True
#             print('new')
#             cart_obj = Cart.objects.new(user=request.user)
#             request.session['cart_id'] = cart_obj.id
#         print(cart_obj)
#         return cart_obj, new_obj
#
#     def new(self, user=None):
#         user_obj = None
#         if user is not None:
#             if user.is_authenticated:
#                 user_obj = user
#         return self.model.objects.create(user=user_obj)

class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return '%s:%s:%s' % (self.user, self.item, self.quantity)


def post_save_item_quantity(sender, instance, *args, **kargs):
    instance.total_amount = instance.quantity * instance.item.disc_price


pre_save.connect(post_save_item_quantity, sender=Item)


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    products = models.ManyToManyField(Product, blank=True)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # objects = CartManager()

    def __str__(self):
        return str(self.id)


def m2m_changed_cart_receiver(sender, instance, action, *args, **kwargs):
    # print(action)
    if action == 'post_add' or action == 'post_remove' or action == 'post_clear':
        products = instance.products.all()
        total = 0
        for i in products:
            total += i.disc_price
        if instance.subtotal != total:
            instance.subtotal = total
            instance.save()


m2m_changed.connect(m2m_changed_cart_receiver, sender=Cart.products.through)


def pre_save_cart_receiver(sender, instance, *args, **kargs):
    if 0 < instance.subtotal < 4000:
        instance.total = instance.subtotal + 25  # this could account for like shipping charges or tax etc.
    else:
        instance.total = instance.subtotal


pre_save.connect(pre_save_cart_receiver, sender=Cart)
