from django.contrib.auth import models
from django.db.models import fields
from django.db.models.query_utils import Q
from rest_framework import serializers
from players.models import Player
from questions.models import Question
from .models import Submission


class SubmissionSerializer(serializers.ModelSerializer):
    participant = serializers.StringRelatedField()
    problem = serializers.StringRelatedField()

    class Meta:
        model = Submission
        fields = '__all__'


class ProblemForScoreboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = [
            'id',
            'name',
            'score'
        ]


class SubmissionForScoreboardSerializer(serializers.ModelSerializer):
    problem = ProblemForScoreboardSerializer()

    class Meta:
        model = Submission
        fields = [
            'id',
            'problem', ]


class ScoreBoardSerializer(serializers.ModelSerializer):
    submissions = SubmissionForScoreboardSerializer(many=True)

    class Meta:
        model = Player
        fields = ['id',
                  'username',
                  'score',
                  'submissions'
                  ]
