from django.urls import path
from . import views

app_name = "opon_imos"
urlpatterns = [
    # Home page
    path("", views.homepage, name="home"),
]
 