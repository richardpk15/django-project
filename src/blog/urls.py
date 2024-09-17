from django.urls import path

from . import views

app_name = "blog"
urlpatterns = [
    path("clear/", views.clear_table_user, name="clear"),
    path("index/", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("index/success/", views.success, name="success"),
    path("list/", views.list_users, name="list"),
    path("", views.login, name="login"),
]
