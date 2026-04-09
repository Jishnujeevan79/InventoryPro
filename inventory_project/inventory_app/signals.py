from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import OrderItem, Manufacturing

@receiver(post_save, sender=OrderItem)
def update_stock_on_order(sender, instance, created, **kwargs):
    product = instance.product
    order = instance.order

    if order.order_type == 'sale':
        product.quantity -= instance.quantity
    elif order.order_type == 'purchase':
        product.quantity += instance.quantity

    product.save()


@receiver(post_save, sender=Manufacturing)
def update_stock_manufacturing(sender, instance, created, **kwargs):
    raw = instance.raw_material
    output = instance.output_product

    raw.quantity -= instance.input_qty
    output.quantity += instance.output_qty

    raw.save()
    output.save()