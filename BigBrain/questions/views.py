from rest_framework.generics import ListAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from scoreboard.models import Submission
from .serializers import QuestionSerializer
from .models import Question


class Questions(ListAPIView):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()

    def get_serializer(self, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        kwargs['context'] = self.get_serializer_context() | {
            'user': self.request.user}
        return serializer_class(*args, **kwargs)


@api_view(['GET', 'POST'])
def sumbit(request, pk):
    if request.method == 'GET':
        question = QuestionSerializer(Question.objects.get(
            pk=pk), context={'user': request.user})
        return Response(question.data)
    elif request.method == 'POST':
        if request.user.is_authenticated:
            question = Question.objects.get(pk=pk)
            answer = request.data.get('answer', None)
            if(pk == 3):
                answers = ["Are you in pain? How can I help?",
                           "Morty, let's get Schwifty", "I am in great pain, please help me."]
                if answer is not None and answer in answers:
                    if not request.user.hasSubmitted(pk):
                        Submission.objects.create(
                            participant=request.user, problem=question)
                        request.user.score += question.score
                        request.user.save()
                        return Response(status=status.HTTP_200_OK)
                    return Response(status=status.HTTP_208_ALREADY_REPORTED)
                return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
            if answer is not None and answer == question.answer:
                if not request.user.hasSubmitted(pk):
                    Submission.objects.create(
                        participant=request.user, problem=question)
                    request.user.score += question.score
                    request.user.save()
                    return Response(status=status.HTTP_200_OK)
                return Response(status=status.HTTP_208_ALREADY_REPORTED)
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
        return Response(status=status.HTTP_403_FORBIDDEN)
