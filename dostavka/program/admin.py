from django.contrib import admin
from .models import *

admin.site.register(Dish)
admin.site.register(Ingredient)
admin.site.register(Order)
admin.site.register(OrderDish)
admin.site.register(Menu)
admin.site.register(DishIngredient)
admin.site.register(Client)

# Register your models here.


@admin.register(UserRole)
class UserRoleAdmin(admin.ModelAdmin):
    list_display = ('user', 'role')
