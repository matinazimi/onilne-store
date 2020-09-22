from django.db import models
from product.models import Product
from user.models import Profile


class Cart(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, default="")
    date = models.DateField(auto_now=True)
    status = models.BooleanField(default=False)

    @property
    def totalprices(self):
        if self:
            totall_price = 0
            middle_carts = self.middle_cart.all()
            for item in middle_carts:
                totall_price += item.price * item.purchase_number
            return totall_price
        else:
            return None

    @property
    def TotalPro(self):
        s = 0
        mid = self.middle_cart.all()
        for item in mid:
            s += int(item.purchase_number)
        return s

    def __str__(self):
        return str(self.pk)


class Middle_cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, default="",related_name='middle_cart')
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, default="", related_name='middle_cart')
    purchase_number = models.IntegerField()

    @property
    def price(self):
        p = int(self.product.price) * int(self.purchase_number)
        return p


class Finance(models.Model):
    user = models.CharField(max_length=30, null=True, blank=True)
    cart = models.CharField(max_length=30, null=True, blank=True)
    number_product = models.CharField(max_length=30, null=True, blank=True)
    total_price = models.CharField(max_length=30, null=True, blank=True)
    date = models.DateField(auto_now=True)
    done = models.BooleanField()
