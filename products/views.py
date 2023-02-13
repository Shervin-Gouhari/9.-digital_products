from django.shortcuts import render, get_object_or_404, get_list_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import *

class ProductListCreateView(APIView):
    def get(self, request):
        products = get_list_or_404(Product)
        serializer = ProductSerializer(instance=products, many=True, context={"request": request})
        return Response(serializer.data)
    
class ProductRetrieveUpdateDestroyView(APIView):
    def get(self, request, pk):
        product = get_object_or_404(Product, id=pk)
        serializer = ProductSerializer(instance=product, context={"request": request})
        return Response(serializer.data)
    
    
    
    
class CategoryListCreateView(APIView):
    def get(self, request):
        categories = get_list_or_404(Category)
        serializer = CategorySerializer(instance=categories, many=True, context={"request": request})
        return Response(serializer.data)
    
class CategoryRetrieveUpdateDestroyView(APIView):
    def get(self, request, pk):
        category = get_object_or_404(Category, id=pk)
        serializer = CategorySerializer(instance=category, context={"request": request})
        return Response(serializer.data)
    
    
    
    
class FileListCreateView(APIView):
    def get(self, request, product_pk):
        files = get_list_or_404(File, product_id=product_pk)
        serializer = FileSerializer(instance=files, many=True, context={"request": request})
        return Response(serializer.data)
    
class FileRetrieveUpdateDestroyView(APIView):
    def get(self, request, product_pk, pk):
        file = get_object_or_404(File, product_id=product_pk, id=pk)
        serializer = FileSerializer(instance=file, context={"request": request})
        return Response(serializer.data)