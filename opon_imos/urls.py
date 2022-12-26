from django.urls import path
from . import views

app_name = "opon_imos" # represent the namespace in the base.html 
urlpatterns = [
    # Home page
    path("", views.homepage, name="home"),
    # Detail page for all topics.
    path("topics/", views.topics, name="topics"),
    # Detail page for a single topic.
    path("topics/<int:topic_id>/", views.topic, name="topic"),
    # Page for adding a new topic
    path('new_topic/', views.new_topic, name='new_topic'),
]
 