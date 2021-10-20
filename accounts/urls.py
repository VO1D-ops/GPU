from django.urls import path
from accounts import views

app_name = 'accounts'
urlpatterns = [
    path("register/", views.Sign_Up, name="register"),
    path("login/", views.Log_In, name="login"),
    path("logout/", views.Log_Out, name="logout"),
]