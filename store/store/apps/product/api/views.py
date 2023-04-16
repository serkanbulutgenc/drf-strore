# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins

# from rest_framework.generics import get_object_or_404
from store.apps.product.models import Product
from .serializer import ProductSerializer


class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


"""
class ProductListCreateView(
    mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

"""

"""
class ProductRetrieveUpdateDeleteView(
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin,
    generics.GenericAPIView,
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, pk, *args, **kwargs):
        return self.retrieve(request, pk, *args, **kwargs)

    def put(self, request, pk, *args, **kwargs):
        return self.update(request, pk, *args, **kwargs)

    def delete(self, request, pk, *args, **kwargs):
        return self.destroy(request, pk, *args, **kwargs)
"""

""" 
# Via APIView
class ProductListCreateView(APIView):
    def get(self, request):
        qs = Product.objects.all()
        p_serializer = ProductSerializer(instance=qs, many=True)
        return Response(data=p_serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        p_serializer = ProductSerializer(data=request.data)
        if p_serializer.is_valid():
            p_serializer.save()
            return Response(data=request.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=p_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductRetrieveUpdateDeleteView(APIView):
    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        serializer = ProductSerializer(instance=product)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request, pk):
        p_serializer = ProductSerializer(data=request.data)
        if p_serializer.is_valid():
            p_serializer.save()
            return Response(data=request.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=p_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
"""

"""
# via decorators
@api_view(["GET", "POST"])
def product_list_create_view(request) -> Response:
    if request.method == "GET":
        qs = Product.objects.all()
        p_serializer = ProductSerializer(instance=qs, many=True)
        return Response(data=p_serializer.data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        p_serializer = ProductSerializer(data=request.data)
        if p_serializer.is_valid():
            p_serializer.save()
            return Response(data=request.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=p_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(["GET", "PUT", "DELETE"])
def product_retrieve_update_delete_view(request, pk: int) -> Response:
    if request.method == "PUT":
        product = get_object_or_404(Product, pk=pk)
        serializer = ProductSerializer(instance=product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "GET":
        product = get_object_or_404(Product, pk=pk)
        serializer = ProductSerializer(instance=product)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    elif request.method == "DELETE":
        product = get_object_or_404(Product, pk=pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
"""
