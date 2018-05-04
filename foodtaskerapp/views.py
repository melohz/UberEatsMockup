from django.shortcuts import render

# Create your views here.
def home(request):
    # if you have any data to pass, input in {}
    return render(request, 'home.html', {}) 