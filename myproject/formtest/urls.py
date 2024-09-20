from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('x', views.hello_template, name='templatetest'),
    path('f', views.get_name, name='formtest01'),
    path('thanks', views.thanks, name='thanks'),
]