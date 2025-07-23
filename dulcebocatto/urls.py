from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from tienda.views import CategoriaViewSet, ProductoViewSet, ClienteViewSet, PedidoViewSet, DetallePedidoViewSet

router = routers.DefaultRouter()
router.register(r'categorias', CategoriaViewSet)
router.register(r'productos', ProductoViewSet)
router.register(r'clientes', ClienteViewSet)
router.register(r'pedidos', PedidoViewSet)
router.register(r'detalles-pedido', DetallePedidoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),  # 👈 importante
]