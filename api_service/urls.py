from django.urls import path, include

from rest_framework import routers

from . import views



router = routers.SimpleRouter()
router.register('products', views.ProductView)
router.register('category', views.CategorylView)
router.register('subcategory', views.SubCatView)
router.register('cultural', views.CulturalView)
router.register('clothing', views.ClothingView)
router.register('brand', views.BrandView)
router.register('image', views.ImageView)
router.register('comment', views.CommentView)
router.register('digital', views.DigitalView)
router.register('homeApp', views.HomeAppView)
router.register('cosmetic', views.CosmeticView)
router.register('cart', views.CartView)
router.register('middlecart', views.BuyingView)
router.register('buy', views.BuyingView,basename='buy')
router.register('factor', views.FactorView)
router.register('search', views.SearchView,basename='search')






urlpatterns = [
    path('', include(router.urls))
]
