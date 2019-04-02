from django.urls import path

from . import views

app_name = 'my_admin'

urlpatterns = [
    path('/index', views.index, name='index'),
    path('/manage', views.ManageUser, name='manage'),
    path('<int:id>/info', views.Info, name='info'),
    path('<int:id>/change', views.Change, name='change'),
    path('/saveinfo', views.SaveInfo, name='saveinfo'),
    path('<int:id>/delete', views.Delete, name='delete')


]
