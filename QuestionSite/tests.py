from django.test import TestCase
from django.utils import timezone
from django.contrib.auth.models import User
import datetime
from .models import Question, MainComment, SubComment


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

class MainCommentModelTest(TestCase):

    def create_question(self):
        user = User.objects.create(username='test_user')
        Question.objects.create(title="Test", description="text", pub_date=timezone.now(), author=user)
        return Question.objects.all()[0]

    def test_if_comment_created(self):
        question = self.create_question()
        self.assertEqual(len(question.maincomment_set.all()), 0)
        MainComment.objects.create(text="Test Comment", related_question=question)
        self.assertEqual(len(question.maincomment_set.all()), 1)

    def test_if_text_correct(self):
        question = question = self.create_question()
        MainComment.objects.create(text="Test Comment", related_question=question)
        self.assertEqual(question.maincomment_set.all()[0].text, 'Test Comment')
