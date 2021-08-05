from django.forms import forms, ModelForm
from .models import Question, Choice

# Alternative way to create a form
# class CreateQuestionForm(forms.Form):
#     question_text = forms.CharField(label='Question text', requred=True)


# I prefer this way, adding via ModelForm
class CreateQuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ['question_text', ]


class CreateChoiceForm(ModelForm):
    class Meta:
        model = Choice
        fields = ['choice_text', ]
