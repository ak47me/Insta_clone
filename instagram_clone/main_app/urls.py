from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("", views.index, name= "main"),
    path("register/", views.register, name="register"),
    path("login/", views.loginPage, name="login"),
    path("chat/", views.chat, name="chat"),
    path('followers_count/', views.followers_count, name='followers_count'),
    path('profile/', views.profile_page, name='profile_page'),
    path('nav/', views.nav, name='nav'),
    path("home/", views.home, name="home"), 
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('logout/', views.logoutUser, name='logout'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)