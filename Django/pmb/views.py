from __future__ import unicode_literals
from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

def index(request):

	return HttpResponse("Welcome to PMB!")

def keyboard(request):

	return 	JsonResponse({
		'type': 'buttons',
		'buttons': ['PMB 시작하기','취소하기']
		})

@csrf_exempt
def message(request):
	message = ((request.body).decode('utf-8'))
	return_json_str = json.loads(message)
	return_str = return_json_str['content']
	
	if (return_str=='PMB 시작하기'):
		return JsonResponse({
			'message': {
				'text': "안녕하세요! PMB입니다.\n베스트셀러를 원하십니까?"
			},
			'keyboard': {
				'type': 'buttons',
				'buttons': ['베스트셀러입니다','베스트셀러 아닙니다']
			}
		})
	elif (return_str=='베스트셀러입니다'or return_str=='베스트셀러 아닙니다'):
		return JsonResponse({
			'message': {
				'text': "스테디셀러를 원하십니까?"
			},
			'keyboard': {
				'type': 'buttons',
				'buttons': ['스테디셀러입니다','스테디셀러 아닙니다']
			}
		})
	elif (return_str=='스테디셀러입니다'or return_str=='스테디셀러 아닙니다'):
		return JsonResponse({
			'message': {
				'text': "신간도서를 원하십니까?"
			},
			'keyboard': {
				'type': 'buttons',
				'buttons': ['신간도서입니다','신간도서 아닙니다']
			}
		})
	elif (return_str=='신간도서 아닙니다'):
		return JsonResponse({
			'message': {
				'text': "출판 연도가 어떻게 됩니까?"
			},
			'keyboard': {
				'type': 'buttons',
				'buttons': ['2000년 이전','2000년-2010년','2010년 이후']
			}
		})
	elif (return_str=='신간도서입니다'or return_str=='2000년 이전'or return_str=='2000년-2010년'or return_str=='2010년 이후'):
		return JsonResponse({
			'message': {
				'text': "국내도서입니까?"
			},
			'keyboard': {
				'type': 'buttons',
				'buttons': ['국내도서입니다','국내도서 아닙니다']
			}
		})
	elif (return_str=='국내도서입니다'or return_str=='국내도서 아닙니다'):
		return JsonResponse({
			'message': {
				'text': "소설입니까?"
			},
			'keyboard': {
				'type': 'buttons',
				'buttons': ['소설입니다','소설 아닙니다']
			}
		})
	elif (return_str=='소설입니다'):
		return JsonResponse({
			'message': {
				'text': "무슨 종류입니까?"
			},
			'keyboard': {
				'type': 'buttons',
				'buttons': ['추리','호러','로맨스']
			}
		})
	elif (return_str=='소설 아닙니다'):
		return JsonResponse({
			'message': {
				'text': "무슨 종류입니까?"
			},
			'keyboard': {
				'type': 'buttons',
				'buttons': ['수필','기행문','자서전']
			}
		})
	elif (return_str=='추리'or return_str=='호러'or return_str=='로맨스'or return_str=='수필'or return_str=='기행문'or return_str=='자서전'):
		return JsonResponse({
			'message': {
				'text': "단편입니까?"
			},
			'keyboard': {
				'type': 'buttons',
				'buttons': ['단편입니다','시리즈입니다']
			}
		})
	elif (return_str=='단편입니다'or return_str=='시리즈입니다'):
		return JsonResponse({
			'message': {
				'text': "가격은 어떻게 됩니까?"
			},
			'keyboard': {
				'type': 'buttons',
				'buttons': ['만원 이내','만원-3만원','3만원 이상']
			}
		})
	elif (return_str=='만원 이내'or return_str=='만원-3만원'or return_str=='3만원 이상'):
		return JsonResponse({
			'message': {
				'text': "모든 질문에 응답을 마쳤습니다.\n결과를 보시겠습니까?"
			},
			'keyboard': {
				'type': 'buttons',
				'buttons': ['결과를 보겠습니다','다시 하겠습니다']
			}
		})
	elif (return_str=='다시 하겠습니다'):
		return JsonResponse({
			'message': {
				'text': "PMB를 다시 시작하시겠습니까?"
			},
			'keyboard': {
				'type': 'buttons',
				'buttons': ['PMB 시작하기','취소하겠습니다']
			}
		})
	else:
		return JsonResponse({
			'message': {
				'text': "취소하겠습니다."
			},
			'keyboard': {
				'type': 'buttons',
				'buttons': ['취','소']
			}
		})

