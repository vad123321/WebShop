from django.shortcuts import render
from .models import Category, Producer, Product
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
    # -> 1
    categories = Category.objects.all()
    producers = Producer.objects.all()
    products = Product.objects.all()

    # -> 2
    selected_category_id = request.GET.get('category')
    selected_producer_id = request.GET.get('producer')

    # -> 3
    if selected_category_id:
        products = products.filter(category_id=selected_category_id)
    if selected_producer_id:
        products = products.filter(producer_id=selected_producer_id)

    # -> 4 ...

    # -> 5 Pagination
    page_size = 10
    paginator = Paginator(products, page_size)
    page = request.GET.get('page')
    # -> 6
    try:
        paginated_products = paginator.page(page)
    except PageNotAnInteger:
        paginated_products = paginator.page(1)
    except EmptyPage:
        paginated_products = paginator.page(paginator.num_pages)
    # -> 7
    return render(request, 'catalog/index.html', context={
        'title': 'Каталог',
        'page': 'index',
        'app': 'catalog',
        'categories': categories,
        'producers': producers,
        'products': paginated_products,
        'selected_category_id': selected_category_id,
        'selected_producer_id': selected_producer_id,
    })
