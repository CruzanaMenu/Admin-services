from django.contrib import admin
from .models import Customer , Comida , Bebida, Pedido

# admin.site.register(Customer)
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name','pub_date']

@admin.register(Comida)
class ComidaAdmin(admin.ModelAdmin):
    list_display = ['id','name_food','desc_small','price']

@admin.register(Bebida)
class BebidasAdmin(admin.ModelAdmin):
    list_display = ['id','desc_bebida','price']

@admin.register(Pedido)
class PedidosAdmin(admin.ModelAdmin):
    list_display = ['id','date_pedido']