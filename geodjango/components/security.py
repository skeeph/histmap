from django.urls import reverse_lazy

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'c51(apjr$4p@o!n=5h-v=2r01ikbug1#k&u-*7nr13x9^#-o0n'

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


LOGIN_REDIRECT_URL = reverse_lazy('profile')
LOGIN_URL = reverse_lazy('login')
LOGOUT_URL = reverse_lazy('logout')

