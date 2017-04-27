from django import forms
from .models import QueryModel
from .models import SurveyModel

class QueryForm(forms.ModelForm):
	class Meta:
		model = QueryModel
		fields = ('title',)

class SurveyForm(forms.ModelForm):
	class Meta:
		model = SurveyModel
		fields = ('q1', 'q2', 'q3', 'q4', 'q5',)
