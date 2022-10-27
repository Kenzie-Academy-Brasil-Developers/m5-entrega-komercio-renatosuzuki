from .serializers import ProductSerializer, ProductDetailedSerializer, ProductGetDetailSerializer
from .models import Product
from .permissions import OwnProductSellerPermission, AuthSellerPermission
from utils.mixins import SerializerByMethodMixin
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication

class ProductView(SerializerByMethodMixin, generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [AuthSellerPermission]
    
    queryset = Product.objects.all()
    serializer_map = {
        "GET": ProductSerializer,
        "POST": ProductDetailedSerializer
    }


    def perform_create(self, serializer):
        serializer.save(seller=self.request.user)


class ProductDetailView(SerializerByMethodMixin, generics.RetrieveUpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [OwnProductSellerPermission]
    
    queryset = Product.objects.all()
    serializer_map = {
        "GET": ProductGetDetailSerializer,
        "PATCH": ProductDetailedSerializer
    }