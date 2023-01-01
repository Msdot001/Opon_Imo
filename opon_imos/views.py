from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Topic, Entry
from .forms import TopicForm, EntryForm

# Create your views here.
def homepage(request):
    """The home page for Opon imo"""
    return render(request, "home.html")


@login_required  # only register user can access to this function
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
                "opon_imos:topics"
            )  # redirect the user back to the topics page after they submit their topic

    # Display a blank or invalid form.
    context = {"form": form}
    return render(request, "new_topic.html", context)


def new_entry(request, topic_id):
    """Add a new entry for a particular topic."""
    topic = Topic.objects.get(id=topic_id)

    if request.method != "POST":
        # No data submitted; create a blank form.
        form = EntryForm()
    else:
        # POST data submitted; process data.
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect("opon_imos:topic", topic_id=topic_id)

    # Display a blank or invalid form.
    context = {"topic": topic, "form": form}
    return render(request, "new_entry.html", context)


def edit_entry(request, entry_id):
    """Edit an existing entry."""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic  # geting topic associated with the entry

    if request.method != "POST":
        # Initial request; pre-fill form with the current entry.
        form = EntryForm(instance=entry)

    else:
        # POST data submitted; process data.
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("opon_imos:topic", topic_id=topic.id)

    context = {"entry": entry, "topic": topic, "form": form}

    return render(request, "edit_entry.html", context)
