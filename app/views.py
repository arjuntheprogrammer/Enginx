from django.shortcuts import render

# Create your views here.

import requests
import json
from django.http import JsonResponse


# requests.post(url, params=params, data=json.dumps(data), headers=headers)
def index(request):
	ec= request.GET.get("ec")
	ph= request.GET.get("ph")
	device = request.GET.get("device")
	moisture= request.GET.get("moisture")
	print(ec, ph, moisture, device)

	# headers = {'content-type': 'application/json'}
	# data = {}
	# params = {'sessionKey': '9ebbd0b25760557393a43064a92bae539d962103', 'format': 'xml', 'platformId': 1}
	url = 'https://wovkld4mh8.execute-api.ap-south-1.amazonaws.com/farmbuddy/?ec='+ec+'&ph='+ph+'&moisture='+moisture+'&device='+device
	r = requests.get(url)
	print(r.content)

	return JsonResponse({"data": str(r.content)})

def position(request):
	lon= request.GET.get("long")
	lat= request.GET.get("lat")
	device = request.GET.get("device")
	print(lon, lat)

	url = 'https://hanwco8wl6.execute-api.ap-south-1.amazonaws.com/farmbuddy/?device='+device+'&long='+lon+'&lat='+lat
	r = requests.get(url)
	print(r.content)

	return JsonResponse({"data": str(r.content)})


def position2(request):
	lon= request.GET.get("long")
	lat= request.GET.get("lat")
	ph = request.GET.get("ph")
	date = request.GET.get("date")
	# print(lon, lat)

	url = 'https://hq3705ecre.execute-api.ap-south-1.amazonaws.com/farmbuddy/?lat='+lat+'&long='+lon+'&ph='+ph+'&date='+date

	# url = 'https://hanwco8wl6.execute-api.ap-south-1.amazonaws.com/farmbuddy/?device='+device+'&long='+lon+'&lat='+lat
	r = requests.get(url)
	print(r.content)

	return JsonResponse({"data": str(r.content)})
