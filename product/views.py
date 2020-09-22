from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView

from .models import *
from finance.models import *


class CategoryView(ListView):
    model = Catagory
    template_name = 'shop-grid.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        p = Cart.objects.all().filter(user_id=self.request.user.id)
        obj = get_object_or_404(Catagory, pk=self.kwargs.get('category_id'))
        cate = Catagory.objects.get(pk=self.kwargs.get('category_id'))
        sd = obj.subcategory.all()
        pr = Product.objects.all().filter(category_id=self.kwargs.get('category_id'))
        context['product'] = pr
        context['category_name'] = obj
        context['num'] = p
        context['category'] = cate
        context['subcategory'] = sd

        return context


class ProductShow(DetailView):
    model = Product
    template_name = 'shop-details.html'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        obj = self.get_object()
        user = self.request.user
        if not obj.digital == 'None':
            digital = obj.digital
        if not obj.homeapplience == 'None':
            homeapp = obj.homeapplience
        if not obj.cultural == 'None':
            cul = obj.cultural
        if not obj.cultural == 'None':
            clo = obj.clothing
        if not obj.number == '0':
            pronum = obj.number
        else:
            pronum = None
        context['product'] = obj
        context['digital'] = digital
        context['cul'] = cul
        context['clo'] = clo
        context['homeapp'] = homeapp
        context['user'] = user
        context['pronum'] = pronum
        return context
