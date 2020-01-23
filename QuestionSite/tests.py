from django.test import TestCase
from django.utils import timezone
from django.contrib.auth.models import User
import datetime
from .models import Question, MainComment, SubComment


class UserManipulationMethods:

    def create_user(self, username):
        return User.objects.create(username=username)


class QuestionManipulationMethods(UserManipulationMethods):

    def create_question(self, title, desc, pub_date, author):
        return Question.objects.create(title=title, description=desc, pub_date=pub_date, author=author)

    def create_question_with_author(self, title, desc, pub_date, username):
        user = self.create_user(username)
        return self.create_question(title, desc, pub_date, user)


class CommentManipulationMethods:

    def create_comment_to_question(self, text, author, question):
        return MainComment.objects.create(text=text, author=author, related_question=question)

    def create_subcomment(self, text, author, comment):
        return SubComment.objects.create(text=text, author=author, related_comment=comment)


class QuestionModelTests(TestCase, QuestionManipulationMethods):

    """
    Here we only checks if methods of Question model are working. We use here reference to its objects.
    """

    def test_if_is_published_future(self):
        """
        Create question with some data and future published date. Method is_published() should return False for this
        object.
        """
        question = self.create_question_with_author(title="Test", desc="text",
                                                    pub_date=timezone.now() + datetime.timedelta(seconds=1),
                                                    username='Test_user')
        self.assertIs(question.is_published(), False)

    def test_if_is_published_past(self):
        """
        Create question with some data and past published date. Method is_published() should return True for this
        object.
        """
        question = self.create_question_with_author(title="Test", desc="text",
                                                    pub_date=timezone.now() - datetime.timedelta(seconds=1),
                                                    username='Test_user')
        self.assertIs(question.is_published(), True)

    def test_if_is_recently_true(self):
        """
        Create question with some data and past published date, one second before 3 days.
        Method was_published_recently() will check if publish date is older than 3 days.
        Should return True.
        """
        question = self.create_question_with_author(title="Test", desc="text",
                                                    pub_date=timezone.now() - datetime.timedelta(days=2, hours=23, minutes=59, seconds=59),
                                                    username='Test_user')
        self.assertIs(question.was_published_recently(), True)

    def test_if_is_recently_false_future(self):
        """
        Create question with some data and future published date.
        Method was_published_recently() will check if publish date is older than 3 days and if question hasn`t been
        published yet.
        Should return False.
        """
        question = self.create_question_with_author(title="Test", desc="text",
                                                    pub_date=timezone.now() + datetime.timedelta(seconds=1),
                                                    username='Test_user')
        self.assertIs(question.was_published_recently(), False)

    def test_if_is_recently_false_past(self):
        """
        Create question with some data and past published date, one second after 3 days.
        Method was_published_recently() will check if publish date is older than 3 days.
        Should return False.
        """
        question = self.create_question_with_author(title="Test", desc="text",
                                                    pub_date=timezone.now() + datetime.timedelta(days=3, seconds=1),
                                                    username='Test_user')
        self.assertIs(question.was_published_recently(), False)


class MainCommentModelTest(TestCase, QuestionManipulationMethods, CommentManipulationMethods):

    def test_if_comment_created(self):
        """
        Firstly, method will create question. Next it will check if there is no comments related to this question.
        At the end it create comment related to previous question with unique author.
        Second assert will check in DB if there is one new comment related.
        (There is no point to use reference to created objects in assert functions, because object could be created
        properly, but in database it could be broken. We see on the website things existing in DB, not in script.)
        """
        question = self.create_question_with_author(title="Test", desc="text", pub_date=timezone.now(),
                                                    username='Test_user')
        self.assertEqual(len(question.maincomment_set.all()), 0)
        comment_auth = self.create_user('comment')
        main_comment = self.create_comment_to_question(text="Comment", author=comment_auth, question=question)
        self.assertEqual(len(question.maincomment_set.all()), 1)

    def test_if_text_correct(self):
        """
        Firstly, method will create question. Next it will check if there is no comments related to this question.
        At the end it create comment related to previous question with unique author.
        Second assert will check if text from db object is the same as text we use to create it.
        (There is no point to use reference to created objects in assert functions, because object could be created
        properly, but in database it could be broken. We see on the website things existing in DB, not in script.)
        """
        question = self.create_question_with_author(title="Test", desc="text", pub_date=timezone.now(),
                                                    username='Test_user')
        comment_auth = self.create_user('comment')
        main_comment = self.create_comment_to_question(text="Test Comment", author=comment_auth, question=question)
        self.assertEqual(question.maincomment_set.all()[0].text, 'Test Comment')

class SubCommentModelTest(TestCase):
    pass


