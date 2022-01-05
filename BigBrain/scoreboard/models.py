from django.db import models
from players.models import Player
from questions.models import Question


class Submission(models.Model):
    participant = models.ForeignKey(
        Player,
        on_delete=models.CASCADE,
        related_name='submissions',)
    problem = models.ForeignKey(
        Question,
        related_name='submissions',
        on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'Player: {self.participant.username}, Question: {self.problem.name}'
