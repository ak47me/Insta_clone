from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name= "main"),
    path("register/", views.register, name="register"),
    path("login/", views.loginPage, name="login"),
    path("chat/", views.chat, name="chat")
]