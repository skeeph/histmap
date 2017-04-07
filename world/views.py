from django.shortcuts import render
from world.forms import DateForm


# Create your views here.
def world(request):
    form = DateForm()
    return render(request, 'world/index.html', {'form': form})
