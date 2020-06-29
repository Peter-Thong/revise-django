from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
# Create your views here.

def home_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    return render(request, "home.html", {})

def contact_view(request, *args, **kwargs):

    context = {
        "my_user": "hello thong",
        "phone_number": 477234,
        "my_list": [313,213,3123,'alall']
    }
    return render(request, "contact.html", context)

def product_detail_view(request):
    obj = Product.objects.get(id=1)
    context = {
        'object': obj
    }
    return render(request, "product/detail.html", context)
