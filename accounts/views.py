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

def register(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data["password"])
            new_user.save()
            user_profile = Profile.objects.create(user=new_user, slug=slugify('{f} {l}'.format(f=new_user.first_name,
                                                                                               l=new_user.last_name),
                                                                              allow_unicode=True))
            user_profile.save()
            return render(request,
                          'registration/register_done.html',
                          {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request,
                  'registration/register.html',
                  {'user_form': user_form})