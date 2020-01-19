from django.contrib import admin
from .models import Question, Answer


class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Text', {'fields': ['question_text', 'question_description']}),
        ('Data information', {'fields': ['question_pub_date']})
    ]
    inlines = [AnswerInline]
    list_display = ('question_text', 'question_pub_date', 'was_published_recently')
    list_filter = ['question_pub_date']
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)
