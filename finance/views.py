from django.shortcuts import render, redirect
from django.views import View

from product.views import *
from product.models import *


class FinanceView(View):

    def post(self, request, *args, **kwargs):

        product_id = request.POST['products_id']
        numbers = request.POST['number']
        pn = Product.objects.get(id=product_id)
        try:

            g = Middle_cart.objects.get(product_id=product_id)

            f = int(g.purchase_number) + int(numbers)
        except:
            f = int(numbers)
        if int(f) > int(pn.number):
            return render(request, 'search.html', {'notpro': pn})
        createmiddlecart(request, product_id, numbers)

        carts = Cart.objects.get(user_id=request.user.id)
        middlcart = Middle_cart.objects.all().filter(cart_id=carts.id)
        context = {'middle': middlcart,
                   'carts': carts,
                   }
        return render(request, 'shoping-cart.html', context)

    def get(self, request, *args, **kwargs):
        carts = Cart.objects.get(user_id=request.user.id)
        middlcart = Middle_cart.objects.all().filter(cart_id=carts.id)
        context = {'middle': middlcart,
                   'carts': carts,
                   }
        return render(request, 'shoping-cart.html', context)


def Delete_middle(request, pro_id):
    Middle_cart.objects.get(id=pro_id).delete()
    return redirect('add-cart')


def get_or_createcart(request):
    if not Cart.objects.filter(user_id=request.user.id):
        cart = Cart.objects.create(user_id=request.user.id)
        return cart.id
    else:
        cart = Cart.objects.get(user_id=request.user.id)
        return cart.id


def createmiddlecart(request, product_id, numbers):
    cartid = get_or_createcart(request)
    m = Middle_cart.objects.all().filter(product_id=product_id)

    try:
        m = m[0]
        p = int(m.purchase_number) + int(numbers)
        m.delete()
    except:
        p = numbers

    Middle_cart.objects.create(cart_id=cartid, product_id=product_id, purchase_number=p)


def Showfactor(request):
    cart = Cart.objects.get(user_id=request.user.id)
    z = Middle_cart.objects.all().filter(cart_id=cart.id)
    for elm in z:
        elm.product.number = int(elm.product.number) - 1
        elm.product.save()

    factor = Finance.objects.create(user=request.user.username, cart=cart.id, total_price=cart.totalprices,
                                    number_product=cart.TotalPro, done=True)

    context = {
        'factor': factor,
    }
    return render(request, 'factor.html', context)
