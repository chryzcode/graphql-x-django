from django.contrib import admin
from .models import Category, Quizzes, Question, Answer

# Register your models here.
admin.site.register(Category)
admin.site.register(Quizzes)
admin.site.register(Question)
admin.site.register(Answer)