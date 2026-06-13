from django.shortcuts import render, get_object_or_404
from . models import Product
from category.models import Category
from cart.models import CartItem
from django.db.models import Q

from cart.views import _cart_id

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Create your views here.
def store(request, category_slug=None):
    
    categories = None
    products = None
    
    if category_slug != None:
        categories = get_object_or_404(Category, cat_slug=category_slug)
        products = Product.objects.filter(category=categories, is_avalible=True)
        paginator = Paginator(products, 10)  # Show 6 products per page
        page = request.GET.get('page')
        page_products = paginator.get_page(page)
        product_count = products.count()
        
    # this block of code is used without paginator
    # else:
    #     products = Product.objects.filter(is_avalible=True)
    #     product_count = products.count()

    # context = {
    #     'products': products,
    #     'product_count': product_count,
    # }
    #return render(request, 'store/store.html', context)

    else:
        products= Product.objects.filter(is_avalible=True).order_by('id')
        paginator = Paginator(products, 10)  # Show 10 products per page
        page = request.GET.get('page')
        page_products = paginator.get_page(page)
        product_count = products.count()
        
    context ={
        'products': page_products,
        'product_count': product_count,
    }
    return render(request, 'store/store.html', context)


def product_detail(request, category_slug, product_slug):
    try:
        single_product =Product.objects.get(category__cat_slug=category_slug, slug=product_slug)
        in_cart = CartItem.objects.filter(cart__cart_id=_cart_id(request), product=single_product)
    except Exception as e:
        raise e
    context= {
        'single_product': single_product,
        'in_cart': in_cart,
    }
    return render(request, 'store/product_detail.html', context)




def search(request):
    products = Product.objects.none()
    product_count = 0
    if 'search-keyword' in request.GET:
        keyword = request.GET['search-keyword']

        if keyword:
            products = Product.objects.order_by('-created_date').filter(
                Q(description__icontains=keyword) |
                Q(product_name__icontains=keyword)
            )
            product_count = products.count()

    context = {
        'products': products,
        'product_count': product_count,
    }

    return render(request, 'store/store.html', context)