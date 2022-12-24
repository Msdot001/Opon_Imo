from django.shortcuts import render

# Create your views here.
def homepage(request):
    """The home page for Opon imo"""
    return render(request, "home.html")
