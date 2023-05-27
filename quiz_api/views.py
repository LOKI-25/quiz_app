from rest_framework import generics
from .models import Quiz
from .serializers import QuizSerializer

class QuizListCreateView(generics.CreateAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

class ActiveQuizRetrieveView(generics.ListAPIView):
    queryset = Quiz.objects.filter(status='active')
    serializer_class = QuizSerializer

class QuizResultRetrieveView(generics.RetrieveAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

class AllQuizzesRetrieveView(generics.ListAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
