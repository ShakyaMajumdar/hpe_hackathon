from django.contrib import admin

from .models import Option, Question, Quiz

# pyright: reportUnknownMemberType=false

admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Option)
