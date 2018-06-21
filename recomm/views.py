from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.utils import timezone
from django.utils.encoding import force_str
from .models import QueryModel, SurveyModel
from .forms import QueryForm, SurveyForm
from .engines import engines
from ipware.ip import get_ip

import requests
import random
from urllib.parse import urlencode, parse_qs

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
            response.set_cookie('username_', urlencode({'id':form.cleaned_data['email']}))
            return response
    else:
    	form = QueryForm()

    response = render(request, 'recomm/index.html', {'form': form})
    # try:
    #     counter = request.COOKIES.get('counter')
    # except NoneType:
    response.set_cookie('counter', 0)
    # print("set query")
    return response


# def store(*values):
#     store.values = values or store.values
#     return store.values
#
#
# def store_list(values):
#     # global x
#     return x.append(values)
#
# def get_store_list():
#     return x

def get_playlist(request, pk):
    if request.method == "POST":
        form = SurveyForm(request.POST)
        if form.is_valid():
            print("form is valid")
            # store_list(pk)
            survey = form.save(commit=False)
            survey.user_ip = get_client_ip(request)
            temp_u = request.COOKIES.get('username_')
            survey.user = parse_qs(temp_u)['id'][0]
            # last_query, last_query_playlist = store()
            temp_q = request.COOKIES.get('query')
            last_query = parse_qs(temp_q)['id'][0]

            last_query_playlist = request.COOKIES.get('query_playlist')
            survey.user_input = last_query
            survey.user_output = last_query_playlist
            survey.save()

            response = redirect('get_playlist', pk=survey.pk)

            counter = int(request.COOKIES.get('counter'))+1

            if counter < 3:
                response.set_cookie('counter', counter)
            else:
                response.delete_cookie('counter')
                response = redirect('ending')

            return response
        else:
            response = redirect('get_playlist', pk=10000)
            return response
    else:
        counter = int(request.COOKIES.get('counter'))
        print(counter)
        query = engines.get_from_test_set(counter)
        print(query)
        algo_result, _ = engines.get_playlist_by_query(query, 2)
        gt_result = engines.get_gt_playlist_by_query(query)
        cosim_result = engines.get_cosim_playlist_by_query(query)

        query_playlist= [(x, 'a') for x in algo_result] \
                        + [(x,'g') for x in gt_result] \
                        + [(x,'c') for x in cosim_result]
        random.shuffle(query_playlist)
        # print(query_playlist)
        # store(query, query_playlist)

        songs_url_list = []
        for song_id, label in query_playlist:
            # print(song_id)
            song_url = "http://music.bugs.co.kr/newPlayer/secureUrl?track_id=%d&format=aac_128" % int(song_id)
            r_song_url = requests.get(url=song_url)

            song_meta = "http://music.bugs.co.kr/player/track/%d" % int(song_id)
            r_song_meta = requests.get(url=song_meta)
            meta_json = r_song_meta.json()['track']

            songs_url_list.append((meta_json['track_title'], meta_json['artist_disp_nm'], r_song_url.json()['secureUrl'], label))

        form = SurveyForm()
        # t = loader.get_template('recomm/playlist.html')
        # c = {'query': query, 'query_playlist': songs_url_list, 'form': form}
        response = render(request, 'recomm/playlist.html', {'query': query, 'query_playlist': songs_url_list, 'form': form, 'counter':int(10-(counter+1))})
        # print(query)
        # response = HttpResponse(t.render(c, request))
        response.set_cookie('query', urlencode({'id':query}))
        response.set_cookie('query_playlist', query_playlist)

    return response


def ending(request):
    response = render(request, 'recomm/ending.html')
    return response
