from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='homepage'),
    path('signup/',views.signup,name='signup'),
    path('profile/',views.profile,name='profile'),
    path('login/',views.userlogin,name='login'),
    path('logout/',views.userlogout,name='logout'), 
    path('passwordchange/',views.changepass,name='passwordchange'), 
    path('passwordchange2/',views.changepass2,name='passwordchange2'), 
]