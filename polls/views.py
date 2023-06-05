from .models import Poll, Question
from .serializers import PollSerializer, QuestionSerializer
from django.shortcuts import get_list_or_404
from rest_framework import viewsets
from rest_framework.response import Response


class PollViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer


class QuestionViewSet(viewsets.ViewSet):
    serializer_class = QuestionSerializer

    def list(self, request, poll_pk=None):
        queryset = get_list_or_404(Question, poll=poll_pk)
        serializer = QuestionSerializer(queryset, many=True)
        return Response(serializer.data)
