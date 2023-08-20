from django.urls import path, include 
from . import views

app_name = "users"

urlpatterns = [ 
    # Include default auth urls. for login and logout 
    path("", include('django.contrib.auth.urls')),
    # path for registration of new users
    path("register/", views.register, name="register"),
]




