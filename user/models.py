from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User


class Profile(models.Model):
    '''in this class user's of DjSaM Market can create profile'''

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    sex_options = [
        ('M', 'Male'),
        ('F', 'Female')
    ]
    gender = models.CharField(max_length=1, null=True, choices=sex_options)
    status = models.BooleanField(default=False)
    join_date = User.date_joined
    is_admin = User.is_staff

    def __str__(self):
        return self.user.username

    image = models.ImageField(upload_to='uploads/', null=True, blank=True)


class Address(models.Model):
    '''in this class users can create multiple adresses'''
    profile = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    STATE_CHOICE = [
        ('Alborz', 'Alborz'),
        ('Ardabil', 'Ardabil'),
        ('Azerbaijan, East', 'Azerbaijan, East'),
        ('Azerbaijan, West', 'Azerbaijan, West'),
        ('Bushehr', 'Bushehr'),
        ('Chahar Mahaal and Bakhtiari', 'Chahar Mahaal and Bakhtiari'),
        ('Fars', 'Fars'),
        ('Gilan', 'Gilan'),
        ('Golestan', 'Golestan'),
        ('Hamadan', 'Hamadan'),
        ('Hormozgān', 'Hormozgān'),
        ('Ilam', 'Ilam'),
        ('Isfahan', 'Isfahan'),
        ('Kerman', 'Kerman'),
        ('Kermanshah', 'Kermanshah'),
        ('Khorasan, North', 'Khorasan, North'),
        ('Khorasan, Razavi', 'Khorasan, Razavi'),
        ('Khorasan, South ', 'Khorasan, South'),
        ('Khuzestan', 'Khuzestan'),
        ('Kohgiluyeh and Boyer - Ahmad', 'Kohgiluyeh and Boyer - Ahmad'),
        ('Kurdistan', 'Kurdistan'),
        ('Lorestan', 'Lorestan'),
        ('Markazi', 'Markazi'),
        ('Mazandaran', 'Mazandaran'),
        ('Qazvin', 'Qazvin'),
        ('Qom', 'Qom'),
        ('Semnan', 'Semnan'),
        ('Sistan, and Baluchestan', 'Sistan and Baluchestan'),
        ('Tehran', 'Tehran'),
        ('Yazd', 'Yazd'),
        ('Zanjan', 'Zanjan'),

    ]
    state = models.CharField('استان', max_length=30,
                             help_text='استان', choices=STATE_CHOICE, null=True)
    city = models.CharField('شهر', max_length=30, help_text='شهر', null=True)
    address = models.CharField('آدرس', max_length=50, null     =True)

    def __str__(self):
        return self.profile.username


class Phones(models.Model):
    '''in this class users can create multiple phone'''

    profile = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    mobile_regx = r'^9\d{9}$'
    mobile_regx = RegexValidator(regex=mobile_regx, message='''try again! You did't follow
                                                                the format''')
    mobile_number = models.CharField(validators=[mobile_regx], max_length=10)
    work_number = models.CharField(max_length=20, blank=True)
    home_number = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.profile.username
