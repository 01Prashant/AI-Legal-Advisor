from django.urls import path, include
from Gen_AI_App.views import *

urlpatterns = [
    # path("admin/", include('Gen_AI_App.urls')),
    path("", HomeView.as_view(), name="home"),
    path('chat/', ChatBot.as_view(), name='chat'),
    path('accounts/', include('allauth.urls')),
    path("accounts/login/", LoginView.as_view(), name="login"),
    path("accounts/logout/", LogoutView.as_view(), name="logout"),
    path("signup/", SignupView.as_view(), name="sign"), 
] 