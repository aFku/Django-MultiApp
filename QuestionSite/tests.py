from django.test import TestCase
from django.utils import timezone
import datetime
from .models import Question


class QuestionModelTests(TestCase):

    def test_if_is_published_future(self):
        question = Question(title="Test", description="text", pub_date=timezone.now() + datetime.timedelta(seconds=1))
        self.assertIs(question.is_published(), False)

    def test_if_is_published_past(self):
        question = Question(title="Test", description="text", pub_date=timezone.now() - datetime.timedelta(seconds=1))
        self.assertIs(question.is_published(), True)

    def test_if_is_recently_true(self):
        question = Question(title="Test", description="text", pub_date=timezone.now() - datetime.timedelta(days=2, hours=23, minutes=59, seconds=59))
        self.assertIs(question.was_published_recently(), True)

    def test_if_is_recently_false_future(self):
        question = Question(title="Test", description="text", pub_date=timezone.now() + datetime.timedelta(seconds=1))
        self.assertIs(question.was_published_recently(), False)

    def test_if_is_recently_false_past(self):
        question = Question(title="Test", description="text", pub_date=timezone.now() + datetime.timedelta(days=3, seconds=1))
        self.assertIs(question.was_published_recently(), False)
