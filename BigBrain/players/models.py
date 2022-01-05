from django.db import models
from django.contrib.auth.models import AbstractUser


class Player(AbstractUser):
    score = models.IntegerField(default=0)
    name = models.CharField(max_length=200)

    def hasSubmitted(self, questionID):
        return self.submissions.filter(problem_id=questionID).exists()
