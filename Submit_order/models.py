from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    power = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 11)])
    image = models.ImageField(upload_to='product_images')
    description = models.TextField()


class Order(models.Model):
    products = models.ManyToManyField(Product, through='OrderItem')


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
