
from django.urls import path,include
from django.contrib.auth import views as auth_views
from . import views

app_name = 'chung'

urlpatterns = [
    path('', views.user_login, name='login'),
    path('logout', views.user_logout, name='logout'),
    path('/checkinfo', views.CheckInfo, name='checkinfo'),
    path('/changeinfo', views.ChangeInfo, name='changeinfo'),
    path('/signup1', views.SignUp1, name='signup1'),
    path('chung/signup2', views.SignUp2, name='signup2'),
    path(r'/activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),

     path(r'/activate_pass/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate_pass, name='activate_pass'),
    path('/resetpass1', views.ResetPass, name='resetpass1'),
    path('chung/resetpass2', views.ResetPass2, name='resetpass2')
    # path('/changepass', views.ChangePass, name='changepass'),
    # path('/savepass', views.ChangePass, name='savepass')
]
