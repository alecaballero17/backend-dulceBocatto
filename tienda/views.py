from rest_framework import viewsets, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
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

        errores = []

        for detalle in detalles_data:
            producto_id = detalle.get("producto")
            if not producto_id:
                errores.append({"error": "Falta el campo 'producto' en un detalle"})
                continue
            try:
                producto = Producto.objects.get(id=producto_id)
                DetallePedido.objects.create(
                    pedido=pedido,
                    producto=producto,
                    cantidad=detalle.get("cantidad", 1)
                )
            except Producto.DoesNotExist:
                errores.append({"producto_id": producto_id, "error": "Producto no encontrado"})

        pedido.refresh_from_db()
        response_serializer = self.get_serializer(pedido)

        if errores:
            return Response({
                "pedido": response_serializer.data,
                "advertencias": errores
            }, status=status.HTTP_201_CREATED)

        return Response(response_serializer.data, status=status.HTTP_201_CREATED)

class DetallePedidoViewSet(viewsets.ModelViewSet):
    queryset = DetallePedido.objects.all()
    serializer_class = DetallePedidoSerializer
