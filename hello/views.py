from django.db.models import Q, F
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View, ListView, CreateView

from .forms import CreateQuestionForm, CreateChoiceForm
from .models import Question, Choice


class Index(View):
    def get(self, request):
        return HttpResponse('<a href = "polls">Polls</a>')


class QuestionsList(ListView):
    template_name = 'hello/questions.html'
    model = Question
    context_object_name = 'questions'

    def get_queryset(self):
        return Question.objects.filter(is_opened=True).order_by('question_text')[:50]


class QuestionPage(View):

    def get(self, request, id_):
        question = get_object_or_404(Question, id=id_)
        choices = Choice.objects.filter(question=question)
        is_voted = Choice.objects.filter(Q(votes=request.user) & Q(question=question)).select_related()

        return render(request, 'hello/question.html', {'question': question, 'choices': choices, 'is_voted': is_voted})

    def post(self, request, id_):
        question = get_object_or_404(Question, id=id_)
        choices = Choice.objects.filter(question=question)
        is_voted = Choice.objects.filter(Q(votes=request.user) & Q(question=question)).select_related()

        for choice in choices:
            if request.POST.get("q" + str(question.id)) == 'c' + str(choice.id):
                if not choice.votes.filter(id=request.user.id).exists():
                    choice.votes.add(request.user)
                    Choice.objects.filter(id=choice.id).update(votes_amount=F('votes_amount') + 1)
                    return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))

        return render(request, 'hello/question.html', {'question': question, 'choices': choices, 'is_voted': is_voted})


class CreatePoll(CreateView):
    form_class = CreateQuestionForm
    template_name = 'hello/create-question.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class

        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            saved_poll = form.save()
            return redirect('create_choice', id_=saved_poll.id)

        return render(request, self.template_name, {'form': form})


class CreatePollChoices(CreateView):
    form_class = CreateChoiceForm
    template_name = 'hello/create-choice.html'

    def get(self, request, id_):
        form = self.form_class
        question = get_object_or_404(Question, id=id_)
        choices = Choice.objects.filter(question=question)

        return render(request, self.template_name, {'form': form, 'question': question, 'choices': choices})

    def post(self, request, id_):
        form = self.form_class(request.POST)
        question = get_object_or_404(Question, id=id_)
        choices = Choice.objects.filter(question=question)

        if form.is_valid():
            Choice.objects.create(question=question, choice_text=form.cleaned_data['choice_text'])
            if choices.count() >= 2:
                Question.objects.filter(id=id_).update(is_opened=True)
            return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))

        return render(request, self.template_name, {'form': form, 'question': question, 'choices': choices})
