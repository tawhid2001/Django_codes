from django.urls import path
from . import views

urlpatterns = [
    path('register/',views.register,name='register'),
    path('login/',views.user_login,name='user_login'),
    path('logout/',views.user_logout,name='user_logout'),
    path('profile/',views.profile,name='profile'),
    path('profile/edit',views.editProfile,name='editProfile'),
    path('profile/edit/password_change/',views.change_password,name='pass_change'),
]