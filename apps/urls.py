from django.urls import include,path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('register/',views.register, name='register'),
    path('login/',views.login, name='login'),
    path('logout/',views.logout_view, name='logout'),
    path('<str:username>/feedback',views.feedback_view, name='feedback'),
    path('<str:username>/edit',views.editprofile, name='editprofile'),
    path('<str:username>/',views.profile, name='profile'),
    path('<str:username>/changeprofilepic/',views.profilepic, name='profilepic'),
    
]
