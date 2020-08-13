from django.urls import path
from . import views


urlpatterns = [
    path("",views.index, name="index"),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('error/', views.doctorsearch, name='error'),
    path('doctor/', views.doctor, name='doctor'),
    path('medicine/', views.medicine, name='medicine'),
    path('delete/<str:pk>/', views.delete_pres, name='delete_pres'),
    path('deletedonner/<str:pk>/', views.delete_donner, name='delete_donner'),

    path('pres_show/', views.pres_show, name='pres_show'),
    path('p/', views.p, name='p'),
    path('loginuser/', views.loginuser, name='loginuser'),
    path('register/', views.register, name='register'),
    path('logoutuser/', views.logoutuser, name='logoutuser'),
    path('doctorsearch/', views.doctorsearch, name='doctorsearch'),
    path('donner/', views.donner, name='donner'),
    path('donnershow/', views.donnershow, name='donnershow'),

]