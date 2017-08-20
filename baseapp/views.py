from django.shortcuts import render_to_response
from django.http import HttpResponse
import json
from Images import matcher
from Images import search_data
from time import time
# Create your views here.


def default(request):
	return render_to_response('index.html')


def match_list(request):
	t1 = time()
	name = request.GET.get('name')
	matcherObj = matcher.main.match(name)	
	colorObj = search_data.main.color_d(name)
	res = dict(matcher=matcherObj, color=colorObj, time=time() - t1)
	return HttpResponse(json.dumps(res), content_type='application/json')