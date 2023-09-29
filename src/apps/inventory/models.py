from django.db import models

from apps.shop.models import Product

class StockRecord(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='stockrecords')
    sku = models.CharField(max_length=64, null=True, blank=True)
    buy_price = models.PositiveBigIntegerField(null=True, blank=True)
    sale_price = models.PositiveBigIntegerField()
    stock_count = models.PositiveIntegerField(default=0)
    threshold_low_stack = models.PositiveIntegerField(null=True, blank=True)
    
    class Meta:
        pass