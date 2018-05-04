from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return redirect(restaurant_home)

# to use this anotation, user will be always asked to have authentification.
# Once loggin out, then user will be asked to login to go to next page.
@login_required(login_url='/restaurant/sign-in/')
def restaurant_home(request):
    return render(request, 'restaurant/home.html', {})