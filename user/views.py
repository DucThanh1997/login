# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, decorators, logout
from chung.models import *
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import reverse, get_object_or_404
from django.core.validators import validate_email
import re

from chung.forms import SignupForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from chung.tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.hashers import check_password,make_password
# Create your views here.

@decorators.login_required(login_url='/')
def index(request):
    return render(request, 'user/index.html')

def SaveInfo(request):
        user = MyUsers.objects.get(username=request.user.username)
        user.fullname = request.POST['ten']
        # check số điện thoại
        if re.match(r'0[0-9\s.-]{9,13}', request.POST['sđt']) == None:
            return JsonResponse({"status": "False", "messages": 'Sai'})
        else:
            user.sdt = request.POST['sđt']

        # check mail
        try:
            validate_email(request.POST['email'])
        except validate_email.ValidationError:
            return JsonResponse({"status": "False", "messages": 'Sai thông tin mail'})
        else:
            user.email = request.POST['email']
        user.save()
        if user.position == 1:
            return JsonResponse({"status": "Done", "messages": reverse('user:index')})
        else:
            return JsonResponse({"status": "Done", "messages": reverse('my_admin:index')})


