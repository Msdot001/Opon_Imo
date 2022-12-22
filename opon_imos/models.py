from django.db import models


class Topic(models.Model):
    """A topic the user is learning about."""

    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model."""
        return self.text


class Entry(models.Model):
    """Something specific learned about a topic."""

    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:  # Meta class holds extra information for managing a model;
        verbose_name_plural = "entries"  # set a special attribute telling Django to use Entries when it needs to refer to more than one entry.

    def __str__(self):
        """Return a string representation of the model."""

        if len(self.content) > 50:
            return f"{self.content[:50]}..."
        else:
            return f"{self.content}"
