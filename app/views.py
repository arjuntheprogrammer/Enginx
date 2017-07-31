from django.shortcuts import render

# Create your views here.

import requests
import json
from django.http import JsonResponse


# requests.post(url, params=params, data=json.dumps(data), headers=headers)
def index(request):
	# headers = {'content-type': 'application/json'}
	# data = {}
	# params = {'sessionKey': '9ebbd0b25760557393a43064a92bae539d962103', 'format': 'xml', 'platformId': 1}
	url = 'https://wovkld4mh8.execute-api.ap-south-1.amazonaws.com/vinayak?ec=13&ph=33&moisture=33'
	r = requests.get(url)
	print(r.content)

	return JsonResponse({"data": str(r.content)})