from django.contrib import admin
from django.urls import path
from quiz_api.views import (
    QuizListCreateView,
    ActiveQuizRetrieveView,
    QuizResultRetrieveView,
    AllQuizzesRetrieveView
)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('quizzes/', QuizListCreateView.as_view(), name='quiz-list-create'),
    path('quizzes/active/', ActiveQuizRetrieveView.as_view(), name='active-quiz-retrieve'),
    path('quizzes/<int:pk>/result/', QuizResultRetrieveView.as_view(), name='quiz-result-retrieve'),
    path('quizzes/all/', AllQuizzesRetrieveView.as_view(), name='all-quizzes-retrieve'),
]


