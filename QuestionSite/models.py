from django.db import models
import datetime
from django.utils import timezone
from django.contrib.auth.models import User


class Question(models.Model):
    title = models.TextField(max_length=100, default=" ")
    description = models.TextField(max_length=255, default=" ")
    pub_date = models.DateTimeField(default=timezone.now)
    create_date = datetime.datetime.now()
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, default=None)

    def is_published(self):
        return timezone.now() >= self.pub_date

    def was_published_recently(self):
        return timezone.now() - datetime.timedelta(days=3) <= self.pub_date <= timezone.now()

    def __str__(self):
        return self.title


class Answer(models.Model):
    related_question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.TextField(max_length=100, default="")
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.answer_text


class CommentInterface(models.Model):
    text = models.TextField(max_length=100, default=" ")
    likes = models.IntegerField(default=0)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.text


class MainComment(CommentInterface):
    related_question = models.ForeignKey(Question, on_delete=models.CASCADE)


class SubComment(CommentInterface):
    related_comment = models.ForeignKey(MainComment, on_delete=models.CASCADE)


class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.TextField(max_length=100, blank=True)
    registration_date = models.DateTimeField()
    first_name = models.TextField(max_length=50, blank=False)
    last_name = models.TextField(max_length=50, blank=False)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

