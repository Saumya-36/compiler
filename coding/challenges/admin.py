# challenges/admin.py
from django.contrib import admin
from .models import Challenge, Submission, TestCase

admin.site.register(Challenge)
admin.site.register(Submission)
admin.site.register(TestCase)
