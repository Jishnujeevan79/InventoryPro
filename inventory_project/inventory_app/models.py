from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    quantity = models.IntegerField()
    description = models.TextField()
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    ORDER_TYPE = (
        ('sale', 'Sale'),
        ('purchase', 'Purchase'),
    )

    STATUS = (
        ('quotation', 'Quotation'),
        ('packing', 'Packing'),
        ('dispatch', 'Dispatch'),
        ('completed', 'Completed'),
    )

    order_type = models.CharField(max_length=10, choices=ORDER_TYPE)
    status = models.CharField(max_length=20, choices=STATUS, default='quotation')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.order_type} - {self.status}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()


class Manufacturing(models.Model):
    raw_material = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='raw')
    output_product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='output')
    input_qty = models.IntegerField()
    output_qty = models.IntegerField()
    status = models.CharField(max_length=20)