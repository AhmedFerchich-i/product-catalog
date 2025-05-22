from django.shortcuts import render
from requests import Request
from .models import Product
# Create your views here.
def product_list(request):
    products=Product.objects.select_related('image','category').all()
    context={'products':products}
    return render(request,'productCatalog/catalog.html',context=context)