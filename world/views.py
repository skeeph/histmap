from django import views
from django.shortcuts import render, redirect
from world.forms import DateForm, CountryForm


# Create your views here.
def world(request):
    form = DateForm()
    return render(request, 'world/index.html', {'form': form})


class New(views.View):
    template = 'world/new.html'
    FormClass = CountryForm

    def get(self, request, *args, **kwargs):
        form = self.FormClass()
        return render(request, 'world/new.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.FormClass(request.POST)
        if form.is_valid():
            new_country = form.save(commit=False)
            lat, lon = new_country.mpoly.coords[0][0][0]
            new_country.lon = lon
            new_country.lat = lat
            new_country.creator = request.user.profile
            new_country.published = False
            new_country.save()
            return redirect("world:map")
        return render(request, 'world/new.html', {'form': form})
