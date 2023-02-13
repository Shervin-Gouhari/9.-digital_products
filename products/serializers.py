from rest_framework import serializers
from .models import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['title', 'description', 'avatar']
        
class FileSerializer(serializers.ModelSerializer):
    file_type =  serializers.SerializerMethodField('get_file_type')
    class Meta:
        model = File
        fields = ['id', 'title', 'file_type', 'file']
    
    def get_file_type(self, file_object):
        return file_object.get_file_type_display()
        
class ProductSerializer(serializers.HyperlinkedModelSerializer):
    categories = CategorySerializer(many=True)
    files = FileSerializer(many=True)
    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'avatar', 'categories', 'files', 'url']