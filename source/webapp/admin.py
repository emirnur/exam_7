from django.contrib import admin

from webapp.models import Choice, Poll

admin.site.register(Poll)
admin.site.register(Choice)
