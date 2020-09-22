from django.urls import path

from .views import *

urlpatterns = [
    path('addcart/<int:user_id>', number, name='add-cart'),
    path('delete/<int:pro_id>', Delete_middle, name='delete-middle'),
    path('factor/', Showfactor, name='factor'),
]
