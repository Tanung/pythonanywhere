from django.contrib import admin

from .models import Question, Choice, Title, TypeStory

admin.site.register(Question)

admin.site.register(Choice)

admin.site.register(Title)

admin.site.register(TypeStory)