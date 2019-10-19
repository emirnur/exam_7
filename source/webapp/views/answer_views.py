from django.shortcuts import render, redirect
from django.views import View
from webapp.models import Answer, Poll, Choice


class AnswerView(View):
    template_name = 'answer/answer.html'

    def get(self, request, *args, **kwargs):
        context = {}
        context['poll'] = Poll.objects.get(pk=kwargs['pk'])
        return render(request, self.template_name, context=context)


    def post(self, request, *args, **kwargs):
        choice_pk = request.POST.get('choice')
        choice = Choice.objects.get(pk=choice_pk)
        poll = Poll.objects.get(pk=kwargs['pk'])
        Answer.objects.create(poll=poll, choice=choice)
        return redirect('index')





