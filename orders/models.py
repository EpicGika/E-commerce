from django.db import models
from django.contrib.auth import get_user_model
from products.models import Product

User = get_user_model()


ORDER_STATUSES = (
    ('Pending', 'Pending'),
    ('Completed', 'Completed'),
    ('Delivered', 'Delivered')
)
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, related_name='orders')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='orders')
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=25,choices=ORDER_STATUSES, default='Pending')

