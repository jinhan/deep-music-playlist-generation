from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.query_input, name='query_input'),
	url(r'^playlist/(?P<pk>[0-9]+)/$', views.get_playlist, name='get_playlist')
]