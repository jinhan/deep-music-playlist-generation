from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.open_query_input, name='open_query_input'),
	url(r'^playlist/(?P<pk>[0-9]+)/$', views.open_get_playlist, name='open_get_playlist')
]
