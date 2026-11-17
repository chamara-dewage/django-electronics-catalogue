
from django.contrib import admin
from django.urls import path
from products import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.product_list, name='product_list'),
    path(
        'category/<str:category_name>/',
        views.products_by_category,
        name='products_by_category'),
    path(
        'tag/<str:tag_name>/',
        views.products_by_tag,
        name='products_by_tag'),
    path(
        'search/',
        views.product_search,
        name='product_search'),
    path(
        'sort/',
        views.product_sort,
        name='product_sort'   
    ),
    path('pagination/', views.product_pagination, name='product_pagination'),
    
]
