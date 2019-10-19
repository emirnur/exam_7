from django import forms

from webapp.models import Poll


class PollForm(forms.ModelForm):
    class Meta:
        model = Poll
        exclude = ['created_at', 'updated_at']