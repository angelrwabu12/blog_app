from django.urls import path
from . views import home,about,contact,login,readmore,addblog
from .import views

urlpatterns = [
    path('', home, name='home'),
    path('about/',about,name='about'),
    path('contact/',contact,name='contact'),
    path('login/',login,name='login'),
    path('readmore/<int:pk>/',readmore,name='readmore'),
    path('addblog/',addblog,name='addblog'),
    path('registration/',views.registration,name='registration'),
]
