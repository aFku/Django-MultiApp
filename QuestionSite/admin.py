from django.contrib import admin
from .models import Question, Answer

"""Adding Question model to admin panel. Now we can create this from there."""

admin.site.register(Question)
admin.site.register(Answer)
