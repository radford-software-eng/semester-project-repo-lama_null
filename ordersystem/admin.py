from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from ordersystem.models import Order, UserAccount, InventoryItem, Cart, Category, ItemCartRelationship

# Register your models here.
admin.site.register(UserAccount)
admin.site.register(Cart)
admin.site.register(Category)
admin.site.register(InventoryItem)
admin.site.register(ItemCartRelationship)

@admin.register(Order)
class ViewAdmin(ImportExportModelAdmin):
    pass
