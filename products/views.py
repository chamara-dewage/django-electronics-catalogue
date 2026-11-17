from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from .models import Product, Category, Tag




def product_list(request):
    products = Product.objects.select_related(
        'category'
    ).prefetch_related('tags')

    # Search
    query = request.GET.get('q', '')

    if query:
        products = products.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query) |
            Q(category__name__icontains=query)
        ).distinct()

    # Category filter
    selected_category = request.GET.get('category', '')

    if selected_category:
        products = products.filter(
            category__name__iexact=selected_category
        )

    # Tag filter
    selected_tag = request.GET.get('tag', '')

    if selected_tag:
        products = products.filter(
            tags__name__iexact=selected_tag
        ).distinct()

    # Sorting
    sort_by = request.GET.get('sort', 'name')

    allowed_sort_options = [
        'price',
        '-price',
        'name',
        '-name'
    ]

    if sort_by not in allowed_sort_options:
        sort_by = 'name'

    products = products.order_by(sort_by)

    # Pagination
    paginator = Paginator(products, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'products': page_obj,
        'page_obj': page_obj,
        'query': query,
        'categories': Category.objects.all(),
        'tags': Tag.objects.all(),
        'selected_category': selected_category,
        'selected_tag': selected_tag,
        'sort_by': sort_by,
    }

    return render(request, 'products.html', context)



def products_by_category(request, category_name):
    category = get_object_or_404(Category, name__iexact=category_name)

    products = Product.objects.filter(
        category=category
    ).select_related('category').prefetch_related('tags')

    paginator = Paginator(products, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'products': page_obj,
        'page_obj': page_obj,
        'selected_category': category
    }

    return render(request, 'products.html', context)

    
 

def products_by_tag(request, tag_name):
    products = Product.objects.filter(
        tags__name__iexact=tag_name
    ).select_related(
        'category'
    ).prefetch_related('tags').distinct()

    paginator = Paginator(products, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'products': page_obj,
        'page_obj': page_obj,
        'selected_tag': tag_name
    }

    return render(request, 'products.html', context)
    


def product_search(request):
    query = request.GET.get('q', '')

    products = Product.objects.select_related(
        'category'
    ).prefetch_related('tags')

    if query:
        products = products.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query) |
            Q(category__name__icontains=query)
        ).distinct()

    paginator = Paginator(products, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'products': page_obj,
        'page_obj': page_obj,
        'query': query
    }

    return render(request, 'products.html', context)

    
 

def product_sort(request):
    sort_by = request.GET.get('sort', 'name')

    allowed_sort_options = [
        'price',
        '-price',
        'name',
        '-name'
    ]

    if sort_by not in allowed_sort_options:
        sort_by = 'name'

    products = Product.objects.select_related(
        'category'
    ).prefetch_related('tags').order_by(sort_by)

    paginator = Paginator(products, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'products': page_obj,
        'page_obj': page_obj,
        'sort_by': sort_by
    }

    return render(request, 'products.html', context)

  
def product_pagination(request):
    products = Product.objects.select_related(
        'category'
    ).prefetch_related('tags').order_by('name')

    paginator = Paginator(products, 5)

    page_number = request.GET.get('page')

    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'products': page_obj
    }

    return render(request, 'products.html', context)