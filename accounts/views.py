from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.utils.text import slugify

from accounts.forms import UserRegistrationForm
from accounts.models import Profile


@login_required
def profile(request):
    p = Profile.objects.get(user=request.user)

    return render(request, 'registration/profile.html', {
        'profile': p,
    })
