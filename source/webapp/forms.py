from django import forms

from webapp.models import Poll, Choice, Answer


class PollForm(forms.ModelForm):
    class Meta:
        model = Poll
        exclude = ['created_at', 'updated_at']


class ChoicePollForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ['answer_option']


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        exclude = []