from django.shortcuts import render
from django.conf import settings
from g_recaptcha.validate_recaptcha import validate_captcha


# Create your views here.
def index(request):
    return render(request, 'zach/home.html')