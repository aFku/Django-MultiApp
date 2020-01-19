from django.db import models
import datetime
from django.utils import timezone

class Question(models.Model):

    """Model for each one new question. You can ask whatever you want in
    question_text, describe this question in question_description and
    set up publish date"""

    question_text = models.TextField('Question', max_length=100)
    question_description = models.TextField('Description', max_length=255)
    question_pub_date = models.DateTimeField('Date published')

    def was_published_recently(self):
        return timezone.now() - datetime.timedelta(days=1) <= self.question_pub_date <= timezone.now()

    was_published_recently.admin_order_field = 'question_pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

    def __str__(self):
        return self.question_text


class Answer(models.Model):

    """Common model for all choices. question is reference to related Question.
    choice_text is description of choice. votes contains number of votes on this choice."""

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.TextField(max_length=100)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
