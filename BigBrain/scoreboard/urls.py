from django.urls import path
from .views import ScoreBoard, Submissions, UserSubmissions

urlpatterns = [
    path('submissions/my/', UserSubmissions.as_view(), name='user_submissions'),
    path('submissions/', Submissions.as_view(), name='submissions'),
    path('', ScoreBoard.as_view(), name='score_board'),
]
