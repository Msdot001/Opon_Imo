from django.shortcuts import render, redirect
from .models import Topic
from .forms import TopicForm, EntryForm

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


def new_topic(request):
    """Add a new topic."""

    if request.method != "POST":
        # No data submitted; create a blank form.
        form = TopicForm()

    else:
        # POST data submitted; process data.
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(
                "opons_imos:topics"
            )  # redirect the user back to the topics page after they submit their topic

    # Display a blank or invalid form.
    context = {"form": form}
    return render(request, "new_topic.html", context)

def new_entry(request, topic_id):
    """Add a new entry for a particular topic."""
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = EntryForm()
    else:
        # POST data submitted; process data.
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)#
            new_entry.topic = topic
            new_entry.save()
            return redirect('opon_imos:topic', topic_id=topic_id)
    
    # Display a blank or invalid form.
    context = {'topic': topic, 'form': form}
    return render(request, 'opon_imos/new_entry.html', context)