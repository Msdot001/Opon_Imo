from django.shortcuts import render
from .models import Topic

# Create your views here.
def homepage(request):
    """The home page for Opon imo"""
    return render(request, "home.html")


def topics(request):
    """Show all topics."""
    topics = Topic.objects.order_by("date_added")
    context = {"topics": topics}
    return render(request, "topics.html", context)


def topic(request, topic_id):
    """Show a single topic and all its entries."""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by(
        "-date_added"
    )  # To get data through a foreign key relationship, you use the lowercase name of the related model followed by an underscore and the word set
    context = {"topic": topic, "entries": entries}
    return render(request, "topic.html", context)

