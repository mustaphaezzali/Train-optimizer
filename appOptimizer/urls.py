from django.urls import path
from . import views

urlpatterns = [
    path('', views.home , name='home'),
    path('disponibilities', views.disponibilities, name='disponibilities'),
    path('filter', views.filter, name='filter'),
]
