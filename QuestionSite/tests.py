from django.test import TestCase
from django.utils import timezone
import datetime
from .models import Question
from django.urls import reverse


class QuestionModelTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(question_pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(question_pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recently_question(self):
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(question_pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)


def create_question(question_text, question_desc, days):
    return Question.objects.create(question_text=question_text, question_description=question_desc,
                                  question_pub_date=timezone.now() + datetime.timedelta(days=days))


class QuestionIndexViewTest(TestCase):
    def test_no_question(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_questions'], [])

    def test_past_question(self):
        create_question("Past Question", "Hello past", -30)
        response = self.client.get(reverse('index'))
        self.assertQuerysetEqual(response.context['latest_questions'], ['<Question: Past question.>'])

    def test_future_question(self):
        create_question("Future question.", "hello future", days=30)
        response = self.client.get(reverse('index'))
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_questions'], [])

    def test_future_question_and_past_question(self):
        create_question("Past question.", 'hello past', days=-30)
        create_question("Future question.", 'hello future', days=30)
        response = self.client.get(reverse('index'))
        self.assertQuerysetEqual(
            response.context['latest_questions'],
            ['<Question: Past question.>']
        )

    def test_two_past_questions(self):
        create_question("Past question 1.", 'hello past', days=-30)
        create_question("Past question 2.", 'hello future', days=-5)
        response = self.client.get(reverse('index'))
        self.assertQuerysetEqual(
            response.context['latest_questions'],
            ['<Question: Past question 2.>', '<Question: Past question 1.>']
        )