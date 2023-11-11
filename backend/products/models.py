from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=99.9)

    @property
    def sale_price(self):
        # 80% of actual price
        return float("%.2f"%(float(self.price) * 0.8,))
    
    def get_discount(self):
        return 122