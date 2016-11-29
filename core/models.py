from django.db import models


class Product(models.Model):
    product_id = models.CharField(max_length=30)
    type = models.CharField(max_length=30, choices=(('advance', 'Advance'),))
    date = models.DateField(verbose_name='Date')
    amount = models.DecimalField(max_digits=10, decimal_places=3)
    amount_discount = models.DecimalField(max_digits=10, decimal_places=3, null=True, blank=True)


class Investor(models.Model):
    name = models.CharField(max_length=30)


class Purchase(models.Model):
    investor = models.ForeignKey(Investor)
    product = models.ForeignKey(Product)
    amount_to_sell = models.DecimalField(max_digits=10, decimal_places=3)

    @property
    def percentage(self):
        try:
            return (self.amount_to_sell * 100) / self.product.amount
        except Exception as e:
            return None

from core.signals import *
