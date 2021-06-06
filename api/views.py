from api.serializers import ProductSerializer
from api.models import Product
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List' : '/product-list/',
        'Detail View': '/product-detail/<int:id>',
        'Create': '/product-create/',
        'Update': 'product-update/<int:id>',
        'Delete': 'product-delete/<int:id>'
    }
    return Response(api_urls)

@api_view(['GET'])
def ShowAll(request):
    products = Product.objects.all()
    serialiser = ProductSerializer(products, many = True)
    return Response(serialiser.data)

@api_view(['GET'])
def ViewProduct(request, pk):
    product = Product.objects.get(id=pk)
    serialiser = ProductSerializer(product, many = False)
    return Response(serialiser.data)

@api_view(['POST'])
def CreateProduct(request):
    serialiser = ProductSerializer(data = request.data)
    if serialiser.is_valid():
        serialiser.save()
    return Response(serialiser.data)

@api_view(['POST'])
def UpdateProduct(request, pk):
    product = Product.objects.get(id=pk)
    serialiser = ProductSerializer(instance = product, data = request.data)
    if serialiser.is_valid():
        serialiser.save()
    return Response(serialiser.data)

@api_view(['GET'])
def DeleteProduct(request, pk):
    product = Product.objects.get(id=pk)
    product.delete()
    return Response('Item Deleted Successfully')