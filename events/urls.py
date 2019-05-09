from django.urls import path
from.import views

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("login.html/", views.loginpage, name="loginpage"),
]
