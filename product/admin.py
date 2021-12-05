from django.contrib import admin
from product.models import Product, Product_image
from . import models

#admin.site.register(models.Product)
admin.site.register(Product)
admin.site.register(Product_image)
