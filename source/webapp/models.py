from django.db import models


class Poll(models.Model):
    question = models.TextField(max_length=200, null=False, blank=False, verbose_name='Вопрос')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время изменения')

    def __str__(self):
        return self.question


class Choice(models.Model):
    answer_option = models.TextField(max_length=200, null=False, blank=False, verbose_name='Вариант ответа')
    poll = models.ForeignKey('webapp.Poll', on_delete=models.CASCADE, null=False, blank=False, verbose_name='Опрос',
                                 related_name='polls')

    def __str__(self):
        return self.answer_option


class Answer(models.Model):
    poll = models.ForeignKey('webapp.Poll', on_delete=models.CASCADE, null=False, blank=False, verbose_name='Опрос',
                                 related_name='answer_poll')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    choice = models.ForeignKey('webapp.Choice', on_delete=models.CASCADE, null=False, blank=False, verbose_name='Вариант ответа',
                             related_name='answer_poll')