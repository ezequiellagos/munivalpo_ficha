from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.login, name="core_login"),
    path('logout/', views.logout, name="core_logout"),
    path('change_password/', views.change_password, name="change_password"),
]