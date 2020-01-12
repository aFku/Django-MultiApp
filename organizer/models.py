from django.db import models


class Event(models.Model):
    """
    Model which represent a one event like in smartphone calendar.
    title = title :P   / max 100 chars
    desc = You can describe there this event. / max 500 chars
    time = time when event will start
    eventype = type of the event (meeting, birthday party, etc...)
    """

    title = models.CharField(max_length=100)
    desc = models.TextField(max_length=500)
    time = models.DateTimeField(blank=True, null=True)
    eventype_choices = (("Meeting", "Meeting"), ("Birthday party", "Birthday party"), ("Lecture", "Lecture"),
                        ("Shopping time", "Shopping time"), ("Netflix alert", "Netflix alert"), ("Other", "Other"))
    # I had no ideas what choices should I write
    eventype = models.CharField(choices=eventype_choices, default="O", max_length=20)

    """
    post() = method for posting event on website
    """

    def post(self):
        self.save()

    def __str__(self):
        return self.title
