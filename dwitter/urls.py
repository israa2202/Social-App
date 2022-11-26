from django.urls import path
from .views import dashboard ,profile_list , profile
from .views import redirect_view

app_name = "dwitter"

urlpatterns = [

    path('/redirect/', redirect_view),
    path("", dashboard, name="dashboard"),
    path("profile_list/", profile_list, name="profile_list"),
    path("profile/<int:pk>", profile, name="profile"),
    


]