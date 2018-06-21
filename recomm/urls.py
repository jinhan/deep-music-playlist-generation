from django.conf.urls import url
from . import views
# from library.views import UpdateThing

urlpatterns = [
	url(r'^$', views.query_input, name='query_input'),
	url(r'^playlist/(?P<pk>[0-9]+)/$', views.get_playlist, name='get_playlist'),
	url(r'^playlist/ending/$', views.ending, name='ending')

]
