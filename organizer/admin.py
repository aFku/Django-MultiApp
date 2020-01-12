from django.contrib import admin
from .models import Event

admin.site.register(Event)  # allow admin to create Event
