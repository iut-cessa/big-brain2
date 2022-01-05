from rest_framework import serializers
from .models import Question


class QuestionSerializer(serializers.ModelSerializer):
    hasSubmitted = serializers.SerializerMethodField()

    class Meta:
        model = Question
        fields = ['id',
                  'name',
                  'description',
                  'score',
                  'hasSubmitted',
                  'photo',
                  ]

    def get_hasSubmitted(self, object):
        user = self.context.get('user', None)
        if user.is_authenticated:
            return self.context['user'].submissions.filter(id=object.id).exists()
        return False
