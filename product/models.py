from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField(default="", blank=True)
    stock_count = models.IntegerField(help_text="How many items are currently in stock.")

    def __str__(self):
        return self.name


class Product_image(models.Model):
    image = models.ImageField()
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name="images")

    def __str__(self):
        return str(self.image)
