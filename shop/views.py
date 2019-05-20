from django.shortcuts import render
from .models import Category, Product
from cart.forms import CartAddProductForm

# Create your views here.
def product_list(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    context = {
        'products': products,
        'categories': categories
    }
    return render(request, 'list.html', context)

def category_prodcut_list(request, categoryid = 1 ):
    categories = Category.objects.all()
    products = Product.objects.filter(category=categoryid)
    context = {
        'products': products,
        'categories': categories
    }
    return render(request, 'categoryproductlist.html', context)
def product_detail(request, productid):
    id = productid
    produs = Product.objects.get(pk=int(id))
    print(produs.id)
    cart_product_form = CartAddProductForm()
    context = {
        'produs': produs,
        'cart_product_form': cart_product_form,
    }
    return render(request, 'produs.html', context)