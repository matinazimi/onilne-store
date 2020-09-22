from django.db import models


class Catagory(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to='content/images', null=True, blank=True)

    def __str__(self):
        return self.name


class SubCatagory(models.Model):
    catagory = models.ForeignKey(Catagory, on_delete=models.CASCADE, related_name='subcategory')
    catogory_name = models.CharField(max_length=100)

    def __str__(self):
        return self.catogory_name


class Brand(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to='content/images', null=True, blank=True)

    def __str__(self):
        return self.name


class Digital(models.Model):
    screen_size = models.FloatField(max_length=5, blank=True, null=True)
    color = models.CharField(max_length=20, blank=True, null=True)
    ram = models.IntegerField(blank=True, null=True)
    harddisck = models.IntegerField(blank=True, null=True)
    screen_resolution = models.IntegerField(blank=True, null=True)
    os_choices = [
        ('android', 'Android'),
        ('windows', 'Windows'),
        ('windows phone', 'Windows Phone'),
        ('linux', 'Linux'),
        ('ios', 'IOS')
    ]
    os = models.CharField(max_length=15, choices=os_choices, blank=True, null=True)
    cpu = models.CharField(max_length=20, blank=True, null=True)
    touch = models.BooleanField(max_length=1, blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.id)


class Cosmetic(models.Model):
    color = models.CharField(max_length=10)
    gender_chices = [
        ('M', 'Male'),
        ('F', 'Female')
    ]
    gender = models.BooleanField(max_length=1, choices=gender_chices, blank=True, null=True)
    smell = models.CharField(max_length=300, blank=True, null=True)
    country = models.CharField(max_length=20, blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.id)


class Clothing(models.Model):
    size = models.CharField(max_length=200, blank=True)
    gender_chices = [
        ('M', 'Male'),
        ('F', 'Female')
    ]
    gender = models.BooleanField(max_length=5, choices=gender_chices, blank=True, null=True)
    color = models.CharField(max_length=10)
    country = models.CharField(max_length=20, blank=True, null=True)
    material = models.CharField(max_length=100, blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.id)


class HomeApplience(models.Model):
    volume = models.CharField(max_length=10, blank=True, null=True)
    color = models.CharField(max_length=10, blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    size = models.CharField(max_length=30, blank=True, null=True)
    capacity = models.CharField(max_length=100, blank=True, null=True)
    material = models.CharField(max_length=100, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.id)


class Cultural(models.Model):
    creator = models.CharField(max_length=50, blank=True, null=True)
    translator = models.CharField(max_length=50, blank=True, null=True)
    publisher = models.CharField(max_length=50, blank=True, null=True)
    gener = models.CharField(max_length=50, blank=True, null=True)
    duration = models.DurationField()
    year = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.id)


class Imageproduct(models.Model):
    image = models.ImageField(upload_to='static/img', null=True, blank=True)


class Comment(models.Model):
    comment = models.CharField(max_length=1000, null=True, blank=True)


class Product(models.Model):
    cosmetic = models.ForeignKey(Cosmetic, on_delete=models.CASCADE, null=True, blank=True,
                                 related_name='product_cosmetic')
    digital = models.ForeignKey(Digital, on_delete=models.CASCADE, null=True, blank=True,
                                related_name='product_digital')
    clothing = models.ForeignKey(Clothing, on_delete=models.CASCADE, null=True, blank=True,
                                 related_name='product_clothing')
    homeapplience = models.ForeignKey(HomeApplience, on_delete=models.CASCADE, null=True, blank=True,
                                      related_name='product_home')
    cultural = models.ForeignKey(Cultural, on_delete=models.CASCADE, null=True, blank=True,
                                 related_name='product_cultural')
    category = models.ForeignKey(Catagory, on_delete=models.CASCADE, default="")
    sub_catagory = models.ForeignKey(SubCatagory, on_delete=models.CASCADE, default="", related_name='product')
    brands = models.ForeignKey(Brand, on_delete=models.CASCADE, default="")
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=100)
    price = models.CharField(max_length=100, default=None)
    descriptions = models.TextField(max_length=2000, null=True, blank=True)
    add_time = models.DateField(auto_now_add=True, null=True, blank=True)
    image = models.ImageField(upload_to='content/images', blank=True, null=True)
    images = models.ForeignKey(Imageproduct, on_delete=models.CASCADE, default="", blank=True, null=True)
    comments = models.ForeignKey(Comment, on_delete=models.CASCADE, default="", blank=True, null=True)

    class Meta:
        ordering = ['add_time']

    def __str__(self):
        return self.name
