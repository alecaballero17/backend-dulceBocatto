from rest_framework import viewsets
from .models import Categoria, Producto, Cliente, Pedido, DetallePedido
from .serializers import CategoriaSerializer, ProductoSerializer, ClienteSerializer, PedidoSerializer, DetallePedidoSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

    def create(self, request, *args, **kwargs):
        detalles_data = request.data.pop("detalles", [])
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        pedido = serializer.save()

        for detalle in detalles_data:
            DetallePedido.objects.create(pedido=pedido, **detalle)

        # Recargar el pedido con detalles para la respuesta
        pedido.refresh_from_db()
        response_serializer = self.get_serializer(pedido)
        return Response(response_serializer.data, status=status.HTTP_201_CREATED)



class DetallePedidoViewSet(viewsets.ModelViewSet):
    queryset = DetallePedido.objects.all()
    serializer_class = DetallePedidoSerializer
