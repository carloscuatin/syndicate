from django.db.models.signals import post_save, post_delete
from core.models import Purchase, Product


def purchase_post_save(sender, instance=None, created=False, **kwargs):
    if created:
        product = instance.product
        product.amount_discount -= instance.amount_to_sell
        product.save()

def product_post_save(sender, instance=None, created=False, **kwargs):
    if created:
        instance.amount_discount = instance.amount
        instance.save()

def purchase_post_delete(sender, instance=None, created=False, **kwargs):
    product = instance.product
    product.amount_discount += instance.amount_to_sell
    product.save()

post_save.connect(purchase_post_save, sender=Purchase)
post_save.connect(product_post_save, sender=Product)
post_delete.connect(purchase_post_delete, sender=Purchase)
