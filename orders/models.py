from django.db import models
from django import forms
from shop.models import Product
from decimal import *
on_delete=models.DO_NOTHING

# defining what is in the order details
class Order(models.Model):
    SNACK = 'S'
    LUNCH = 'L'
    TIMES = ((SNACK, 'Snack'),
             (LUNCH, 'Lunch')
             )

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    collection = models.CharField(max_length=2, choices=TIMES, default=SNACK)
    homeroom = models.CharField(max_length=20)
    notes_to_Canteen = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


#What is required to make an item
class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product,
                                related_name='order_items', on_delete=models.CASCADE)

    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity