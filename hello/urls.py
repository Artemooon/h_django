from django.urls import path

from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('polls/', views.QuestionsList.as_view(), name="questions_list"),
    path('poll/<int:id_>/', views.QuestionPage.as_view(), name="question_page"),
    path('create-poll', views.CreatePoll.as_view(), name="create_poll"),
    path('create-choice/<int:id_>/',  views.CreatePollChoices.as_view(), name="create_choice")
]
