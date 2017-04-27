from django.db import models
from django.utils import timezone
from likert_field.models import LikertField
from django.contrib.auth.models import User

class QueryModel(models.Model):
	title = models.CharField(max_length=200)
	user = models.CharField(max_length=20)
	created_date = models.DateTimeField(default=timezone.now)

class SurveyModel(models.Model):
	q1 = LikertField('입력한 쿼리와 플레이 리스트가 유사했다.', blank=False)
	q2 = LikertField('플레이 리스트의 노래들이 서로 유사했다.', blank=False)
	q3 = LikertField('seven is my lucky number.', blank=False)
	q4 = LikertField('dgag.', blank=False)
	q5 = LikertField('이 플레이 리스트를 내 친구에게 공유하고 싶다.', blank=False)
	user = models.CharField(max_length=20)
	created_date = models.DateTimeField(default=timezone.now)