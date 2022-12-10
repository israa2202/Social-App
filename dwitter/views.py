from django.shortcuts import render
from .forms import DweetForm
from django.contrib.auth import login
from .models import Profile, Dweet
from django.shortcuts import redirect, redirect
from django.urls import reverse
from social.forms import CustomUserCreationForm




def redirect_view(request):
    response = redirect('/redirect-success/')
    return response

def dashboard(request):
    return render(request, "dwitter/dashboard.html")
def home(request):
    form = DweetForm(request.POST or None)
    if request.method == "POST":
        form = DweetForm(request.POST)
        if form.is_valid():
            dweet = form.save(commit=False)
            dweet.user = request.user
            dweet.save()
            return redirect("dwitter:home")
    followed_dweets = Dweet.objects.filter(
        user__profile__in=request.user.profile.follows.all()
        ).order_by("-created_at")
    return render(request,"dwitter/home.html",{"form": form, "dweets": followed_dweets},
    )
            
    return render(request, "dwitter/home.html", {"form": form})

def profile_list(request):
    profiles = Profile.objects.exclude(user=request.user)
    return render(request, "dwitter/profile_list.html", {"profiles": profiles})    


def profile(request, pk):
    profile = Profile.objects.get(pk=pk)
    if request.method == "POST":
        current_user_profile = request.user.profile
        data = request.POST
        action = data.get("follow")
        if action == "follow":
            current_user_profile.follows.add(profile)
        elif action == "unfollow":
            current_user_profile.follows.remove(profile)
        current_user_profile.save()
    return render(request, "dwitter/profile.html", {"profile": profile})

def register(request):
    if request.method == "GET":
        return render( request, "dwitter/register.html",
            {"form": CustomUserCreationForm})

    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
       


    login(request, user)
    return redirect(reverse("dashboard"))
