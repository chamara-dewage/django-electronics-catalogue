
from django.contrib import admin
from django.urls import path
from products import views


# Define the URL patterns and connect each URL to its corresponding view.
urlpatterns = [

    # Django administration site.
    path('admin/', admin.site.urls),

    # Main product catalogue page.
    path('', views.product_list, name='product_list'),

    # Display products belonging to a specific category.
    path(
        'category/<str:category_name>/',
        views.products_by_category,
        name='products_by_category'),

    # Display products associated with a specific tag.
    path(
        'tag/<str:tag_name>/',
        views.products_by_tag,
        name='products_by_tag'),

    # Search products using a search query.
    path(
        'search/',
        views.product_search,
        name='product_search'),

    # Sort products based on the selected sorting option.
    path(
        'sort/',
        views.product_sort,
        name='product_sort'   
    ),

    # Display products using pagination.
    path('pagination/', views.product_pagination, name='product_pagination'),
    
]
