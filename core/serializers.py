from rest_framework import serializers
from core.models import Product, Investor, Purchase


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class InvestorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Investor
        fields = '__all__'

class PurchaseSerializer(serializers.ModelSerializer):
    percentage = serializers.SerializerMethodField()
    class Meta:
        model = Purchase
        fields = ['id', 'percentage', 'amount_to_sell', 'investor', 'product', 'investor_name']

    def get_percentage(self, obj):
        return obj.percentage

    def get_investor_name(self, obj):
        return obj.investor_name
