from django.urls import path
from .views import *

# app_name = 'products'

urlpatterns = [
    path('categories/', CategoryListCreateView.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryRetrieveUpdateDestroyView.as_view(), name='category-detail'),
    
    path('products/', ProductListCreateView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductRetrieveUpdateDestroyView.as_view(), name='product-detail'),
    
    path('products/<int:product_pk>/files/', FileListCreateView.as_view(), name='file-list'),
    path('products/<int:product_pk>/files/<int:pk>/', FileRetrieveUpdateDestroyView.as_view(), name='file-detail'),
]