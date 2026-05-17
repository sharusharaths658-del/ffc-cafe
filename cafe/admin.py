from django.contrib import admin
from .models import *

admin.site.register(Category)
admin.site.register(MenuItem)
admin.site.register(Variant)
admin.site.register(ItemType)   
admin.site.register(OrderItem)
admin.site.register(Payment)
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer', 'total_amount', 'status', 'created_at']
    list_editable = ['status']