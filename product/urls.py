from django.urls import path

from .views import *

urlpatterns = [
    path('product_detail/<int:pk>', ProductShow.as_view(), name='product-details'),
    path('product/<int:category_id>', CategoryView.as_view(), name='category-sub'),
]
