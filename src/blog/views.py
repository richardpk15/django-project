from django.shortcuts import redirect, render
from django.http import JsonResponse

from .forms import UserForm
from .models import Pessoa

"""def index(request):
    return render(request, "blog/index.html")"""


def index(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("success/")
    else:
        form = UserForm()
    return render(request, "blog/index.html", {"form": form})


def about(request):
    return render(request, "blog/about.html")


def contact(request):
    return render(request, "blog/contact.html")


def success(request):
    return render(request, "blog/success.html")


def list_users(request):
    users = Pessoa.objects.all()
    return render(request, "blog/list.html", {"users": users})


def login(request):
    return render(request, "blog/login.html")


def clear_table_user(request):
    Pessoa.objects.all().delete()
    return render(request, "blog/success.html")
