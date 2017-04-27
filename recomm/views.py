from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import QueryModel, SurveyModel
from .forms import QueryForm, SurveyForm
from .engines import engines 
from ipware.ip import get_ip

import requests

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
    

def query_input(request):
	if request.method == "POST":
		form = QueryForm(request.POST)
		if form.is_valid():
			query = form.save(commit=False)
			query.user = get_client_ip(request)
			query.save()
			response = redirect('get_playlist', pk=query.pk)
			return response
	else:
		form = QueryForm()	

	return render(request, 'recomm/index.html', {'form': form})


def get_playlist(request,pk):
	query = get_object_or_404(QueryModel, pk=pk)
	query_playlist = engines.get_playlist_by_query(query)

	songs_url_list = []
	for song_id in query_playlist:
		song_url = "http://music.bugs.co.kr/newPlayer/secureUrl?track_id=%d&format=aac_128" % song_id
		r_song_url = requests.get(url=song_url)
		
		song_meta = "http://music.bugs.co.kr/player/track/%d" % song_id
		r_song_meta = requests.get(url=song_meta)
		meta_json = r_song_meta.json()['track']

		songs_url_list.append((meta_json['track_title'], meta_json['artist_disp_nm'], r_song_url.json()['secureUrl']))
	

	if request.method == "POST":
		form = SurveyForm(request.POST)
		if form.is_valid():
			survey = form.save(commit=False)
			survey.user = get_client_ip(request)
			survey.save()
			response = redirect('query_input')
			return response
	else:
		form = SurveyForm()	

	return render(request, 'recomm/playlist.html', {'query': query, 'query_playlist': songs_url_list, 'form': form})