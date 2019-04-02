from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import reverse, get_object_or_404
from .models import *
from django.contrib.auth import authenticate, login, decorators, logout
from django.core.exceptions import ObjectDoesNotExist
from django.core.validators import validate_email
import re
from .forms import SignupForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import base36_to_int, int_to_base36
from django.utils.crypto import constant_time_compare, salted_hmac
from django.conf import settings

# Đăng nhập
def user_login(request):
    if request.method == 'POST':
        ten = request.POST['ten']
        password = request.POST['password']
        try:
            user = MyUsers.objects.get(username=ten)
        except ObjectDoesNotExist:
            return JsonResponse({"status": "False", "messages": 'Không tồn tại người dùng này'})
        else:
            my_login = authenticate(username=ten, password=password)
            if my_login is None:
                return JsonResponse({"status": "False", "messages": 'Sai mật khẩu'})
            else:
                login(request, my_login)
                if user.position == 1:
                    return JsonResponse({"status": "Done", "messages": reverse('user:index')})
                elif user.position == 2:
                    return JsonResponse({"status": "Done", "messages": reverse('my_admin:index')})
    elif request.method == 'GET':
        return render(request, 'chung/login.html')

# Đăng xuất
def user_logout(request):
    logout(request)
    return redirect(reverse('chung:login'))


# Xem thông tin người dùng
def CheckInfo(request):
    user = MyUsers.objects.get(username=request.user.username)
    print(user.email)
    if user.position == 1:
        return render(request, 'chung/CheckInfo.html', {'data': user})
    else:
        return render(request, 'chung/CheckInfo-Admin.html', {'data': user})

# Thay đổi thông tin người dùng
def ChangeInfo(request):
    user = MyUsers.objects.get(username=request.user.username)
    if user.position == 1:
        return render(request, 'chung/ChangeInfo.html', {'data': user})
    else:
        return render(request, 'chung/ChangeInfo-Admin.html', {'data': user})

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
        return JsonResponse({"status": "Done", "messages": reverse('user:index')})


def SignUp1(request):
    form = SignupForm()
    return render(request, 'chung/SignUp.html', {'form': form})


def SignUp2(request):
    form = SignupForm(request.POST)
    if form.is_valid():
        user = form.save(commit=False)
        user.is_active = False
        user.save()
        current_site = get_current_site(request)
        mail_subject = 'Xác nhận tài khoản.'
        message = render_to_string('chung/Confirm_mail.html', {
            'user': user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
            'token': default_token_generator.make_token(user),
        })

        to_email = form.cleaned_data.get('email')
        email = EmailMessage(
                    mail_subject, message, to=[to_email]
        )
        email.send()
        return JsonResponse({"status": "Done", "messages": reverse('chung:login')})


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        # print(token)
        user1 = MyUsers.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user1 = None
    if user1 is not None and default_token_generator.check_token(user1, token):
        user1.is_active = True
        user1.save()
        login(request, user1)
        return render(request, 'user/index.html')
    else:
        return render(request, 'chung/Errorr.html')


def activate_pass(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        print(uid)
        user = MyUsers.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return redirect(reverse('chung:login'))
    else:
        return render(request, 'chung/Errorr.html')


def ResetPass(request):
    return render(request, 'chung/Reset_Pass.html')



def ResetPass2(request):
    data = MyUsers.objects.all()
    for x in data:
        if x.username == request.POST['username1']:
            user = MyUsers.objects.get(username=request.POST['username1'])
            user.set_password(request.POST['New_Pass'])
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Xác nhận tài khoản của bạn qua mail.'
            message = render_to_string('chung/Confirm_pass.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                'token': default_token_generator.make_token(user),
            })
            to_email = user.email
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.send()
            return JsonResponse({"status": "Done", "messages": 'okke'})
        else:
            return redirect(reverse('chung:login'))






# def SavePass(request):
#     user = MyUsers.objects.get(username=request.user.username)
#
#     if check_password(request.POST['New_Pass']):
#         user.make_password(request.POST['New_Pass'])
#         user.save()
#         print(1)
#         return JsonResponse({"status": "Done", "messages": reverse('user:index')})
#     else:
#         return JsonResponse({"status": "False", "messages": 'Sai thông tin password'})
#
#
#
# def ChangePass(request):
#     user = MyUsers.objects.get(username=request.user.username)
#     return render(request, 'user/ChangePass.html', {'data': user})



