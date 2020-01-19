from django.db import models


class Question(models.Model):

    """Model for each one new question. You can ask whatever you want in
    question_text, describe this question in question_description and
    set up publish date"""

    question_text = models.TextField('Question', max_length=100)
    question_description = models.TextField('Description', max_length=255)
    question_pub_date = models.DateTimeField('Date published')

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
