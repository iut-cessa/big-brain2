from django.urls import path

from .views import Questions, sumbit

urlpatterns = [
    path('<int:pk>/', sumbit, name='submit'),
    path('', Questions.as_view(), name='list_question'),
]
