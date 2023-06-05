from .models import Poll, Question
from .serializers import PollSerializer, QuestionSerializer
from rest_framework import generics


class PollList(generics.ListAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer


class QuestionList(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
