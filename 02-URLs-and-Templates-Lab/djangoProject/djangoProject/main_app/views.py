from django.shortcuts import render


# Create your views here.

def show_main_app(request):
    return render(request, 'main_app/index.html')
