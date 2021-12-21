from django.shortcuts import render


# Create your views here.

def show_secondary_app(request):
    return render(request, 'secondary_app/index.html')
