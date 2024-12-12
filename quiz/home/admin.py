from django.contrib import admin
from .models import Question, QuizSession, Answer

admin.site.register(Question)
admin.site.register(QuizSession)
admin.site.register(Answer)
