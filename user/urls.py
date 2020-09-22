from django.urls import path

from .views import Login, register, Custom_logout

urlpatterns = [
    path('login/', Login, name='log-in'),
    path('register/', register, name='register'),
    path('logout/', Custom_logout, name='log-out')
]
