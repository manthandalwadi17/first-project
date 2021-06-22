from django.contrib import admin
from .models import Company_Details, Customer_Order,Company_Customers,Company_Product

# Register your models here.
admin.site.register(Company_Details)
admin.site.register(Company_Customers)
admin.site.register(Company_Product)
admin.site.register(Customer_Order)
