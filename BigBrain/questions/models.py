from django.db import models


class Question(models.Model):
    name = models.CharField(max_length=300, unique=True)
    score = models.IntegerField()
    description = models.CharField(max_length=2000)
    answer = models.CharField(max_length=300)
    photo = models.ImageField(blank=True)

    def __str__(self) -> str:
        return self.name
