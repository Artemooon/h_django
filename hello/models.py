from django.db import models
from django.conf import settings


class Question(models.Model):
    question_text = models.CharField(max_length=150)
    pub_date = models.DateTimeField(auto_now=True)
    is_opened = models.BooleanField(default=False)

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)
    votes_amount = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
