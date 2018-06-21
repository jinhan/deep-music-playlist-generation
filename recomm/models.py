from django.db import models
from django.utils import timezone
from likert_field.models import LikertField
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField
# from django import forms

class QueryModel(models.Model):
	email = models.CharField(max_length=200, blank=False)
	male = models.CharField(max_length=5, blank=True)
	female = models.CharField(max_length=5, blank=True)
	birth = models.CharField(max_length=10, blank=False)

	user = models.CharField(max_length=100)
	created_date = models.DateTimeField(default=timezone.now)

# class SurveyModel(models.Model):
# 	checkbox_inline = models.TypedChoiceField(
#     label=_('Checkbox Inline'),
#     widget=models.CheckboxSelectMultiple,
#     choices=((1, 'Inline 1',), (2, 'Inline 2',), (3, 'Inline 3',), (4, 'Inline 4',),)
# )
class SurveyModel(models.Model):
	# q1 = models.CharField(max_length=5, blank=True)
	# q2 = models.CharField(max_length=5, blank=True)
	# q3 = models.CharField(max_length=5, blank=True)
	q1_1_0 = LikertField(blank=False)

	q2_1_1 = models.CharField(max_length=5, blank=True)
	q2_1_2 = models.CharField(max_length=5, blank=True)
	q2_1_3 = models.CharField(max_length=5, blank=True)
	# q2_1_4 = models.CharField(max_length=5, blank=True)
	# q2_1_5 = models.CharField(max_length=5, blank=True)

	q3_1_1 = models.CharField(max_length=5, blank=True)
	q3_1_2 = models.CharField(max_length=5, blank=True)
	q3_1_3 = models.CharField(max_length=5, blank=True)
	# q3_1_4 = models.CharField(max_length=5, blank=True)
	# q3_1_5 = models.CharField(max_length=5, blank=True)
	###
	q1_2_0 = LikertField(blank=False)

	q2_2_1 = models.CharField(max_length=5, blank=True)
	q2_2_2 = models.CharField(max_length=5, blank=True)
	q2_2_3 = models.CharField(max_length=5, blank=True)
	# q2_2_4 = models.CharField(max_length=5, blank=True)
	# q2_2_5 = models.CharField(max_length=5, blank=True)

	q3_2_1 = models.CharField(max_length=5, blank=True)
	q3_2_2 = models.CharField(max_length=5, blank=True)
	q3_2_3 = models.CharField(max_length=5, blank=True)
	# q3_2_4 = models.CharField(max_length=5, blank=True)
	# q3_2_5 = models.CharField(max_length=5, blank=True)
	###
	q1_3_0 = LikertField(blank=False)

	q2_3_1 = models.CharField(max_length=5, blank=True)
	q2_3_2 = models.CharField(max_length=5, blank=True)
	q2_3_3 = models.CharField(max_length=5, blank=True)
	# q2_3_4 = models.CharField(max_length=5, blank=True)
	# q2_3_5 = models.CharField(max_length=5, blank=True)

	q3_3_1 = models.CharField(max_length=5, blank=True)
	q3_3_2 = models.CharField(max_length=5, blank=True)
	q3_3_3 = models.CharField(max_length=5, blank=True)
	# q3_3_4 = models.CharField(max_length=5, blank=True)
	# q3_3_5 = models.CharField(max_length=5, blank=True)
	###
	q1_4_0 = LikertField(blank=False)

	q2_4_1 = models.CharField(max_length=5, blank=True)
	q2_4_2 = models.CharField(max_length=5, blank=True)
	q2_4_3 = models.CharField(max_length=5, blank=True)
	# q2_4_4 = models.CharField(max_length=5, blank=True)
	# q2_4_5 = models.CharField(max_length=5, blank=True)

	q3_4_1 = models.CharField(max_length=5, blank=True)
	q3_4_2 = models.CharField(max_length=5, blank=True)
	q3_4_3 = models.CharField(max_length=5, blank=True)
	# q3_4_4 = models.CharField(max_length=5, blank=True)
	# q3_4_5 = models.CharField(max_length=5, blank=True)
	###
	q1_5_0 = LikertField(blank=False)

	q2_5_1 = models.CharField(max_length=5, blank=True)
	q2_5_2 = models.CharField(max_length=5, blank=True)
	q2_5_3 = models.CharField(max_length=5, blank=True)
	# q2_5_4 = models.CharField(max_length=5, blank=True)
	# q2_5_5 = models.CharField(max_length=5, blank=True)

	q3_5_1 = models.CharField(max_length=5, blank=True)
	q3_5_2 = models.CharField(max_length=5, blank=True)
	q3_5_3 = models.CharField(max_length=5, blank=True)
	# q3_5_4 = models.CharField(max_length=5, blank=True)
	# q3_5_5 = models.CharField(max_length=5, blank=True)
	###
	q1_6_0 = LikertField(blank=False)

	q2_6_1 = models.CharField(max_length=5, blank=True)
	q2_6_2 = models.CharField(max_length=5, blank=True)
	q2_6_3 = models.CharField(max_length=5, blank=True)
	# q2_6_4 = models.CharField(max_length=5, blank=True)
	# q2_6_5 = models.CharField(max_length=5, blank=True)

	q3_6_1 = models.CharField(max_length=5, blank=True)
	q3_6_2 = models.CharField(max_length=5, blank=True)
	q3_6_3 = models.CharField(max_length=5, blank=True)
	# q3_6_4 = models.CharField(max_length=5, blank=True)
	# q3_6_5 = models.CharField(max_length=5, blank=True)

	# q1_1 = models.CharField(max_length=5, blank=False)
	# q1_1 = models.CharField(max_length=5, blank=False)
	# q1_1 = models.CharField(max_length=5, blank=False)

	## likert
	# q1_1 = LikertField(blank=False)
	# # q2_1 = LikertField(blank=False)
	# q1_2 = LikertField(blank=False)
	# # q2_2 = LikertField(blank=False)
	# q1_3 = LikertField(blank=False)
	# # q2_3 = LikertField(blank=False)
	# q1_4 = LikertField(blank=False)
	# # q2_4 = LikertField(blank=False)
	# q1_5 = LikertField(blank=False)
	# # q2_5 = LikertField(blank=False)
	# q1_6 = LikertField(blank=False)
	# # q2_6 = LikertField(blank=False)
	# q1_7 = LikertField(blank=False)
	# # q2_7 = LikertField(blank=False)
	# q1_8 = LikertField(blank=False)
	# # q2_8 = LikertField(blank=False)
	# q1_9 = LikertField(blank=False)
	# q2_9 = LikertField(blank=False)
	# q1_10 = LikertField(blank=False)
	# q2_10 = LikertField(blank=False)

	user = models.CharField(max_length=100)
	user_ip = models.CharField(max_length=20)
	created_date = models.DateTimeField(default=timezone.now)
	user_input = models.CharField(max_length=200)
	user_output = models.CharField(max_length=200)
