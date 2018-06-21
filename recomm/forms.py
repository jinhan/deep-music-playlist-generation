from django import forms
from .models import QueryModel
from .models import SurveyModel


class QueryForm(forms.ModelForm):
	class Meta:
		model = QueryModel
		fields = ('email', 'male', 'female', 'birth',)

class SurveyForm(forms.ModelForm):
	class Meta:
		model = SurveyModel
		# fields = ()
		# fields = ('q1','q2', 'q3',)
		# fields = ('q1_1', 'q2_1','q1_2', 'q2_2','q1_3', 'q2_3','q1_4', 'q2_4',)
		fields = ('q1_1_0',\
		'q2_1_1','q2_1_2','q2_1_3',\
		#'q2_1_4','q2_1_5',\
		'q3_1_1','q3_1_2','q3_1_3',\
		#'q3_1_4','q3_1_5', \
		'q1_2_0',\
		'q2_2_1','q2_2_2','q2_2_3',\
		#'q2_2_4','q2_2_5',\
		'q3_2_1','q3_2_2','q3_2_3',\
		#'q3_2_4','q3_2_5', \
		'q1_3_0',\
		'q2_3_1','q2_3_2','q2_3_3',\
		#'q2_3_4','q2_3_5',\
		'q3_3_1','q3_3_2','q3_3_3',\
		#'q3_3_4','q3_3_5',
		'q1_4_0',\
		'q2_4_1','q2_4_2','q2_4_3',\
		#'q2_4_4','q2_4_5',\
		'q3_4_1','q3_4_2','q3_4_3',\
		#'q3_4_4','q3_4_5',\
		'q1_5_0',\
		'q2_5_1','q2_5_2','q2_5_3',\
		#'q2_5_4','q2_5_5',\
		'q3_5_1','q3_5_2','q3_5_3',\
		#'q3_5_4','q3_5_5', \
		'q1_6_0',\
		'q2_6_1','q2_6_2','q2_6_3',\
		# 'q2_6_4','q2_6_5',
		'q3_6_1','q3_6_2','q3_6_3',) #'q3_6_4','q3_6_5', )
