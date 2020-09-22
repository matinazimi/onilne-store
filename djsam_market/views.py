from django.shortcuts import render
from product.models import Catagory,Product
from finance.models import *
from django.db.models import Q
from django.views.generic.base import View

# def base(request):
#     if request.method == 'GET':
#         return render(request, 'index.html')

# def detail(request):
#     if request.method == 'GET':
#         return render(request, 'shop-details.html')


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
    def get(self, request, *args, **kwargs):
        pass
    #     print('omad')
    #     search_text = request.GET['search']
    #     result = Product.objects.filter(
    #         Q(name__icontains=search_text) |
    #         Q(price__icontains=search_text)
    #     ).distinct()
    #     print('1vomi res', result)
    #     return render(request, 'search.html', {'search_result': result})
    def post(self, request, *args, **kwargs):
        # form = SearchForm(request.POST)
        # search_text = form['search'].value()

        search_text = request.POST['search']
        result = Product.objects.filter(
            Q(name__icontains=search_text) |
            Q(price__icontains=search_text)
        )
        print('2vomi res',result)
        return render(request, 'search.html', {'search_result': result})




