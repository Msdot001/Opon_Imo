from django.urls import path
from . import views

app_name = "opon_imos" # represent the namespace in the base.html 
urlpatterns = [
    # Home page
    path("", views.homepage, name="home"),
]
 