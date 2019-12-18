from django.contrib import admin

from gestion_pedidos.models import Cliente,Articulo,Pedido,Estado,Detalle
# Register your models here.

admin.site.register(Cliente)
admin.site.register(Articulo)
admin.site.register(Pedido)
admin.site.register(Estado)
admin.site.register(Detalle)
