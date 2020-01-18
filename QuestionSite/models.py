from django.db import models


class Question(models.Model):

    """Model for each one new question. You can ask whatever you want in
    question_text, describe this question in question_description and
    set up publish date"""

    question_text = models.TextField('Question', max_length=100)
    question_description = models.TextField('Description', max_length=255)
    question_pub_date = models.DateTimeField('Date published')

class Answer(models.Model):
