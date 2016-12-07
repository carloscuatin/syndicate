from django.db.models.signals import post_save, post_delete, pre_save

from core.models import Purchase, Product


def purchase_post_save(sender, instance=None, created=False, **kwargs):
    if created:
        product = instance.product
        product.amount_discount -= instance.amount_to_sell
        product.save()


def purchase_post_delete(sender, instance=None, created=False, **kwargs):
    product = instance.product
    product.amount_discount += instance.amount_to_sell
    product.save()


def purchase_pre_save(sender, instance=None, **kwargs):
    product = instance.product
    if product and instance.pk:
        old = sender.objects.get(pk=instance.pk)
        product.amount_discount += old.amount_to_sell
        product.amount_discount -= instance.amount_to_sell
        product.save()
        
    if instance.amount_to_sell > instance.product.amount:
        raise Exception("amount_to_sell can't be higher to amount_discount")


def product_post_save(sender, instance=None, created=False, **kwargs):
    if created:
        instance.amount_discount = instance.amount
        instance.save()


post_save.connect(product_post_save, sender=Product)
post_save.connect(purchase_post_save, sender=Purchase)
pre_save.connect(purchase_pre_save, sender=Purchase)
post_delete.connect(purchase_post_delete, sender=Purchase)
