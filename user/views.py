from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from finance.models import *


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User

        fields = ['username', 'email',
                  'password1', 'password2']

        labels = {
            "username": "نام کاربری",
            "email": "ایمیل",
            "password1": "رمز عبور",
            "password2": "تکرار رمز عبور",
        }

        help_texts = {
            'username': 'باید کمتر از 150 کاراکتر باشد',
            "email": "ایمیل خود را به درستی وارد کنید",
        }

    def save(self, commit=True):
        '''
        override user create form to create profile after register!
        '''
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        print('hello1')
        try:
            print('hello2')
            if commit:
                print('hello3')
                user.save()
            Profile.objects.create(user=user)

        except Exception as e:
            user.delete()
            raise ValueError(f"cant create profile object! reason: {e}")

        return user


def register(request):
    print('hello4')
    if request.method == 'POST':
        print('hello5')
        form = CustomUserCreationForm(request.POST)
        print(request.POST['username'])
        if form.is_valid():
            form.save()
            return redirect('log-in')
        else:
            return render(request, 'register.html', {'form': form})

    form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})


def Login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    if request.method == 'POST':
        print('hello2')
        username = request.POST['username']
        password = request.POST['password']

        if authenticate(username=username, password=password):

            user_obj = User.objects.get(username=username)
            login(request, user_obj)
            return redirect("home")
        else:

            return render(request, 'login.html')


def Custom_logout(request):
    logout(request)
    return redirect('home')
