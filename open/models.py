from django.db import models
from django.utils import timezone
from likert_field.models import LikertField
from django.contrib.auth.models import User

class QueryModel(models.Model):
	title = models.CharField(max_length=200)
	user = models.CharField(max_length=20)
	created_date = models.DateTimeField(default=timezone.now)

class SurveyModel(models.Model):
	q1 = LikertField('음악들이 내가 입력한 주제와 잘 부합하였다.', blank=False)
	q2 = LikertField('음악들의 주제가 서로 일관성이 있었다.', blank=False)
	q3 = LikertField('음악들이 나의 니즈를 잘 반영하였다.', blank=False)
	q4 = LikertField('이번에 새롭에 듣게 된 음악들이 있었다.', blank=False)
	q5 = LikertField('이 웹사이트를 주변 사람들에게 추천하겠다.', blank=False)
	user = models.CharField(max_length=20)
	created_date = models.DateTimeField(default=timezone.now)
	user_input = models.CharField(max_length=200)
	user_output = models.CharField(max_length=200)
