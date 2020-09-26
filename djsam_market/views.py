from django.shortcuts import render
from product.models import Catagory,Product
from finance.models import *
from django.db.models import Q
from django.views.generic.base import View




def base(request):
    if request.method == "GET":
        category = Catagory.objects.all()

        pro = Product.objects.all()[:8]
        user=request.user
        p=Cart.objects.all().filter(user_id=request.user.id)
        con = {'category': category,
               'num':p,
               'pro': pro,
               'user':user,

               }

        return render(request, 'home.html', con)







class SearchProduct(View):

    def post(self, request, *args, **kwargs):

        search_text = request.POST['search']
        result = Product.objects.filter(
            Q(name__icontains=search_text) |
            Q(price__icontains=search_text)
        )
        print('2vomi res',result)
        return render(request, 'search.html', {'search_result': result})




