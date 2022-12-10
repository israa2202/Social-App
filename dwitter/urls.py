from django.urls import path, include
from .views import dashboard ,profile_list , profile, home , register
from .views import redirect_view
 

app_name = "dwitter"

urlpatterns = [
    path('/redirect/', redirect_view),
    path("home/", home, name="home"),
    path("profile_list/", profile_list, name="profile_list"),
    path("profile/<int:pk>", profile, name="profile"),
    path("", dashboard, name="dashboard"),
    path("accounts/", include("django.contrib.auth.urls")),
    path('oauth/', include('social_django.urls', namespace='social')), 
    path("register/", register, name="register"),
]