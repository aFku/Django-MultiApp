from django.shortcuts import render
from organizer.models import Event
import datetime


def event_list(request):
    events = Event.objects.all()
    return render(request, "organizer/event_list.html", {"events": events})
