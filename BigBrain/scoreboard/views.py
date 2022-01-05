from rest_framework.decorators import permission_classes
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from players.models import Player
from .serializers import SubmissionSerializer, ScoreBoardSerializer
from .models import Submission


class ScoreBoard(ListAPIView):
    serializer_class = ScoreBoardSerializer
    queryset = Player.objects.all()

    def get(self, *args, **kwargs):
        scoreBoard = Player.objects.all().order_by('-score')
        return Response(ScoreBoardSerializer(scoreBoard, many=True).data)


class Submissions(ListAPIView):
    serializer_class = SubmissionSerializer
    queryset = Submission.objects.all()


class UserSubmissions(ListAPIView):
    serializer_class = SubmissionSerializer
    queryset = Submission.objects.all()
    permission_classes = [IsAuthenticated]

    def get(self, *args, **kwargs):
        submissions = Submission.objects.all().filter(
            participant_id=self.request.user.id)
        return Response(SubmissionSerializer(submissions, many=True).data)
