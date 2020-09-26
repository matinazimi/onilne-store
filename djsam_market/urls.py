"""djsam_market URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import base, SearchProduct
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', base, name='home'),
    path('search/',SearchProduct.as_view() , name='search-pro'),
    path('user/', include('user.urls')),
    path('', include('product.urls')),
    path('', include('finance.urls')),
    path('api/', include('api_service.urls')),
    path('api-token-auth/', obtain_jwt_token),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

# if settings.DEBUG:
#     # static files (images, css, javascript, etc.)
#     urlpatterns += patterns('',
#         (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
#         'document_root': settings.MEDIA_ROOT}))
