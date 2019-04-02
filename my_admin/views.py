from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, reverse
from django.contrib.auth import authenticate, login, decorators, logout
from chung.models import MyUsers
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.core.validators import validate_email
import re
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

@decorators.login_required(login_url='/')
def index(request):
    return render(request, 'my_admin/index.html')

def ManageUser(request):
    data = MyUsers.objects.all()
    return render(request, 'my_admin/Manage.html', {'data': data})

def Info(request, id):
    user = MyUsers.objects.get(id=id)
    return render(request, 'my_admin/Info.html', {'user': user})

def Change(request, id):
    user = MyUsers.objects.get(id=id)
    return render(request, 'my_admin/Change.html', {'user': user})

def SaveInfo(request):
        user = MyUsers.objects.get(id=request.POST['id'])
        if user.fullname != request.POST['fullname']:
            user.fullname = request.POST['fullname']

        if user.sdt != request.POST['sđt']:
            if re.match(r'0[0-9\s.-]{9,13}', request.POST['sđt']) == None:
                return JsonResponse({"status": "False", "messages": 'Sai'})
            else:
                user.sdt = request.POST['sđt']
        print(user.username)
        print(user.email)
        print(request.POST['email'])
        if user.email != request.POST['email']:
            try:
                validate_email(request.POST['email'])
            except validate_email.ValidationError:
                return JsonResponse({"status": "False", "messages": 'Sai thông tin mail'})
            else:
                print(1)
                user.email = request.POST['email']
        user.save()
        if user.position == 1:
            return JsonResponse({"status": "Done", "messages": reverse('user:index')})
        else:
            return JsonResponse({"status": "Done", "messages": reverse('my_admin:index')})

def Delete(request, id):
    try:
        User = MyUsers.objects.get(id=id)
        User.delete()
    except(User.DoesNotExist):
        return render(request, 'my_admin/Info.html', {'user': User})
    else:
        data = MyUsers.objects.all()
        return render(request, 'my_admin/Manage.html', {'data': data})

