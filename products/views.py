from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from .models import Product
from .forms import ProductForm
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


def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()
    context = {
        'form': form
    }
    return render(request, "product/product_create.html", context)


def product_update_view(request, id):
    initial = {
        "title": "hello there"
    }
    obj = get_object_or_404(Product, id=id)
    form = ProductForm(request.POST or None, instance=obj)
    context = {
        'form': form
    }
    return render(request, "product/product_create.html", context)

def product_detail_view(request, id):
    obj = get_object_or_404(Product, id=id)
    context = {
        'object': obj
    }
    return render(request, "product/product_detail.html", context)

def product_delete_view(request, id):
    obj = get_object_or_404(Product, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect("../../")
    context = {
        'object': obj
    }
    return render(request, "product/product_delete.html", context)

def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, "product/product_list.html", context)
