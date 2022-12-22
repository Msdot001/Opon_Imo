from django.urls import path
from . import views

app_name = "lopon_imos"
urlpatterns = [
    # Home page
    path("", views.homepage, name="home"),
]
 