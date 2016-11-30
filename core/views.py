from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from core.models import Product, Investor, Purchase
from core.serializers import ProductSerializer, InvestorSerializer, PurchaseSerializer


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    lookup_field = 'product_id'
    filter_fields = ('product_id', 'date',)


class InvestorViewSet(viewsets.ModelViewSet):
    serializer_class = InvestorSerializer
    queryset = Investor.objects.all()
    lookup_field = 'name'
    filter_fields = ('name',)


class PurchaseViewSet(viewsets.ModelViewSet):
    serializer_class = PurchaseSerializer
    queryset = Purchase.objects.all()
    filter_fields = ('product__id',)
