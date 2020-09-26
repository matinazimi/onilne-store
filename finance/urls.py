from django.urls import path

from .views import *

urlpatterns = [
    path('addcart/', FinanceView.as_view(), name='add-cart'),
    path('delete/<int:pro_id>', Delete_middle, name='delete-middle'),
    path('factor/', Showfactor, name='factor'),
]
