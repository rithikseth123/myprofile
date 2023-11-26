from django.views.generic import View
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from .forms import UserSignUpForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .models import CustomUser
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.


class IndexView(View):
    def get(self, request):
        user = request.user
        # print(user.username, user.email)
        return render(request, "profile/index.html", {"user": user})


def signup(request):
    if request.method == "POST":
        form = UserSignUpForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = True
            user.save()
            return redirect("/")
        else:
            return render(request, "profile/signup.html", {"form": form})
    form = UserSignUpForm()
    return render(request, "profile/signup.html", {"form": form})


def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            u = request.POST["username"]
            p = request.POST["password"]
            user = authenticate(request, username=u, password=p)
            if user is not None:
                auth_login(request, user)
                return redirect("main-page")
            else:
                messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, "profile/login.html", {"form": form})


@login_required
def logout(request):
    auth_logout(request)
    return redirect("main-page")
