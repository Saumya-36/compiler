# challenges/forms.py

from django import forms
from .models import CodingAnswer

class CodingAnswerForm(forms.ModelForm):
    class Meta:
        model = CodingAnswer
        fields = ['answer_text']
