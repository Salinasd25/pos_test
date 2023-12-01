from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework import (
    generics,
    permissions,
    status,
    filters,
)
# APP
from pos_test.models import (
    Product,
)
from pos_test.serializers import (
    ProductSerializer,
)


# Listar productos
class ProductList(generics.ListAPIView):
    """
    Ruta para consultar productos,
    permisos libres temporal
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (
        DjangoFilterBackend,
    )
    filterset_fields = [
        'barcode',
    ]
    authentication_classes = ()
    permission_classes = ()
    pagination_class = None
    
    def get(self, request, *args, **kwargs):
        barcode = self.request.query_params.get('barcode')
        if barcode:
            data = super().get(request, *args, **kwargs)
            if not data.data:
                return Response({"detail":"producto no existe"},status=400)
            
            return Response({"data":data.data[0]},status=200)
        else:
            return Response({'detail':'consulte por codigo de barra'},status=400)
        return super().get(request, *args, **kwargs)
    