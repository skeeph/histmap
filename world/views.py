from django.shortcuts import render


# Create your views here.
def world(request):
    return render(request, 'world/index.html')
