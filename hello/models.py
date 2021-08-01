from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=150)
    pub_date = models.DateTimeField()
    is_opened = models.BooleanField()

    def __str__(self):
        return self.question_text