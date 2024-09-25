from django.urls import path
from . import views

urlpatterns = [
    path('', views.main,name="main"),
    path('signup', views.signup,name="signup"),
    path('login', views.login,name="login"),
    path('privacy', views.privacy,name="privacy"),
    path('team', views.team,name="team"),
    path('chat', views.chat,name="chat"),
    path('bot', views.bot,name="bot"),
    path('index', views.index,name="index"),
    path('signout', views.signout, name='signout'),
   
]