from django.http import HttpResponse
from django.shortcuts import render

from .models import Question


def index(request):
    return HttpResponse('<marquee behavior="scroll" direction="right" scrollamount="30">Hello, world.</marquee>')


def questions_list(request):
    questions = Question.objects.all().order_by('question_text')[:40]

    return render(request, 'hello/questions.html', {"questions": questions})
