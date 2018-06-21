from django.contrib import admin

# Register your models here.
from .models import QueryModel, SurveyModel

admin.site.register(QueryModel)
admin.site.register(SurveyModel)
