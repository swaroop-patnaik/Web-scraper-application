from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/',views.home, name='home'),
    path('segment/', views.segment, name='segment'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
]