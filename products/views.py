
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from .models import Product, Category, Tag


def product_list(request):

    # Retrieve products along with their related categories and tags.
    # select_related() uses a SQL JOIN for the ForeignKey relationship.
    # prefetch_related() retrieves ManyToMany-related tags efficiently.
    products = Product.objects.select_related(
        'category'
    ).prefetch_related('tags')

    # Search products by name, description or category name.
    # Q objects combine multiple search conditions using OR.
    query = request.GET.get('q', '')

    if query:
        products = products.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query) |
            Q(category__name__icontains=query)
        ).distinct()

    # Filter products by the selected category.
    selected_category = request.GET.get('category', '')

    if selected_category:
        products = products.filter(
            category__name__iexact=selected_category
        )

    # Filter products by the selected tag.
    # distinct() prevents duplicate products in the results.
    selected_tag = request.GET.get('tag', '')

    if selected_tag:
        products = products.filter(
            tags__name__iexact=selected_tag
        ).distinct()

    # Sort products by name or price in ascending or descending order.
    # Only predefined sorting options are allowed.
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

    # Divide the filtered and sorted products into pages.
    # Each page displays a maximum of 5 products.
    paginator = Paginator(products, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Prepare the data required by the HTML template.
    # Includes products, available filters and current selections.
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

    # Render the HTML template with the provided data.
    return render(request, 'products.html', context)


def products_by_category(request, category_name):

    # Find the requested category.
    # Return a 404 error if the category does not exist.
    category = get_object_or_404(Category, name__iexact=category_name)

    # Retrieve products belonging to the selected category,
    # including their related category and tag information.
    products = Product.objects.filter(
        category=category
    ).select_related('category').prefetch_related('tags')

    # Divide the category's products into pages of 5.
    paginator = Paginator(products, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Pass the products and selected category to the template.
    context = {
        'products': page_obj,
        'page_obj': page_obj,
        'selected_category': category
    }

    return render(request, 'products.html', context)


def products_by_tag(request, tag_name):

    # Retrieve products associated with the requested tag.
    # Include related category and tag information.
    # distinct() prevents duplicate products from appearing.
    products = Product.objects.filter(
        tags__name__iexact=tag_name
    ).select_related(
        'category'
    ).prefetch_related('tags').distinct()

    # Divide the filtered products into pages of 5.
    paginator = Paginator(products, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Pass the products and selected tag to the template.
    context = {
        'products': page_obj,
        'page_obj': page_obj,
        'selected_tag': tag_name
    }

    return render(request, 'products.html', context)


def product_search(request):

    # Get the search keyword entered by the user.
    query = request.GET.get('q', '')

    # Retrieve products with their related categories and tags.
    products = Product.objects.select_related(
        'category'
    ).prefetch_related('tags')

    # Search by product name, description or category name.
    # Q objects combine the search conditions using OR.
    if query:
        products = products.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query) |
            Q(category__name__icontains=query)
        ).distinct()

    # Divide the search results into pages of 5.
    paginator = Paginator(products, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Pass the search results and keyword to the template.
    context = {
        'products': page_obj,
        'page_obj': page_obj,
        'query': query
    }

    return render(request, 'products.html', context)


def product_sort(request):

    # Get the sorting option selected by the user.
    sort_by = request.GET.get('sort', 'name')

    # Define the sorting options supported by the application.
    allowed_sort_options = [
        'price',
        '-price',
        'name',
        '-name'
    ]

    # Use name as the default if an unsupported option is provided.
    if sort_by not in allowed_sort_options:
        sort_by = 'name'

    # Retrieve products with related category and tag information,
    # then apply the selected sorting option.
    products = Product.objects.select_related(
        'category'
    ).prefetch_related('tags').order_by(sort_by)

    # Divide the sorted products into pages of 5.
    paginator = Paginator(products, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Pass the sorted products and selected sorting option to the template.
    context = {
        'products': page_obj,
        'page_obj': page_obj,
        'sort_by': sort_by
    }

    return render(request, 'products.html', context)


def product_pagination(request):

    # Retrieve all products with their related categories and tags.
    # Sort products by name before applying pagination.
    products = Product.objects.select_related(
        'category'
    ).prefetch_related('tags').order_by('name')

    # Divide the products into pages of 5.
    paginator = Paginator(products, 5)

    # Get the requested page number and retrieve that page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Pass the paginated products to the template.
    context = {
        'page_obj': page_obj,
        'products': page_obj
    }

    return render(request, 'products.html', context)
