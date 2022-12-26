from django.shortcuts import render
from .models import Topic

# Create your views here.
def homepage(request):
    """The home page for Opon imo"""
    return render(request, "home.html")

def topics(request):
    """Show all topics."""
    topics = Topic.objects.order_by("date_added")
    context = {"topics" : topics}
    return render(request, "topics.html", context)
