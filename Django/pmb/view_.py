from __future__ import unicode_literals
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
import random
import os


def index(request):
    return HttpResponse("Welcome to PMB!")


def keyboard(request):
    return JsonResponse({'type': 'buttons', 'buttons': ['PMB 시작하기', '취소하기']})


@csrf_exempt
def message(request):
    message = ((request.body).decode('utf-8'))
    return_json_str = json.loads(message)
    return_str = return_json_str['content']
    f = open('result.txt', 'w')

    if (return_str == 'PMB 시작하기'):
        return JsonResponse({'message': {'text': '안녕하세요! PMB입니다. \베스트셀러를 원하십니까?'},
                             'keyboard': {'type': 'button',
                                          'button': ['베스트셀러입니다', '베스트셀러가 아닙니다']}})
    elif (return_str == '베스트셀러입니다'):
        f.write('베스트셀러\n')
        return JsonResponse({'message': {'text': '스테디셀러를 원하십니까?'},
                             'keyboard': {'type': 'button',
                                          'button': ['스테디셀러입니다', '스테디셀러가 아닙니다']}})
    elif (return_str == '베스트셀러가 아닙니다'):
        return JsonResponse({'message': {'text': '스테디셀러를 원하십니까?'},
                             'keyboard': {'type': 'button',
                                          'button': ['스테디셀러입니다', '스테디셀러가 아닙니다']}})
    elif (return_str == '스테디셀러입니다'):
        f.write('스테디셀러\n')
        return JsonResponse({'message': {'text': '신간 도서를 원하십니까?'},
                             'keyboard': {'type': 'button',
                                          'button': ['신간 도서를 보고 싶습니다', '신간 도서가 아닙니다']}})
    elif (return_str == '스테디셀러가 아닙니다'):
        return JsonResponse({'message': {'text': '신간 도서를 원하십니까?'},
                             'keyboard': {'tyㄴpe': 'button',
                                          'button': ['신간 도서를 보고 싶습니다', '신간 도서가 아닙니다']}})
    elif (return_str == '신간 도서가 아닙니다'):
        return JsonResponse({'message': {'text': '언제 출판된 책이 보고 싶으신가요?'},
                             'keyboard': {'type': 'button',
                                          'button': ['2000년 이전', '2000년-2010년', '2010년 이후']}})
    elif (return_str == '신간 도서를 보고 싶습니다'):
        f.write('신간도서\n')
        return JsonResponse({'message': {'text': '국내 도서입니까?'},
                             'keyboard': {'type': 'button',
                                          'button': ['국내 도서입니다', '국내 도서가 아닙니다']}})
    elif (return_str == '2000년 이전'):
        f.write('2000년이전\n')
        return JsonResponse({'message': {'text': '소설입니까?'},
                             'keyboard': {'type': 'button',
                                          'button': ['소설입니다', '소설이 아닙니다']}})
    elif (return_str == '2000년-2010년'):
        f.write('2000년-2010년\n')
        return JsonResponse({'message': {'text': '소설입니까?'},
                             'keyboard': {'type': 'button',
                                          'button': ['소설입니다', '소설이 아닙니다']}})
    elif (return_str == '2010년 이후'):
        f.write('2010년이후\n')
        return JsonResponse({'message': {'text': '소설입니까?'},
                             'keyboard': {'type': 'button',
                                          'button': ['소설입니다', '소설이 아닙니다']}})
    elif (return_str == '소설입니다'):
        f.write('소설\n')
        return JsonResponse({'message': {'text': '어떤 장르입니까?'},
                             'keyboard': {'type': 'button',
                                          'button': ['추리', '판타지', '로맨스']}})
    elif (return_str == '소설이 아닙니다'):
        return JsonResponse({'message': {'text': '어떤 책입니까?'},
                             'keyboard': {'type': 'button',
                                          'button': ['시', '여행', '자기계발']}})
    elif (return_str == '추리'):
        f.write('추리\n')
        return JsonResponse({'message': {'text': '단편입니까?'},
                             'keyboard': {'type': 'button',
                                          'button': ['단편입니다', '장편입니다', '시리즈입니다']}})
    elif (return_str == '판타지'):
        f.write('판타지\n')
        return JsonResponse({'message': {'text': '단편입니까?'},
                             'keyboard': {'type': 'button',
                                          'button': ['단편입니다', '장편입니다', '시리즈입니다']}})
    elif (return_str == '로맨스'):
        f.write('로맨스\n')
        return JsonResponse({'message': {'text': '단편입니까?'},
                             'keyboard': {'type': 'button',
                                          'button': ['단편입니다', '장편입니다', '시리즈입니다']}})
    elif (return_str == '시'):
        f.write('시\n')
        return JsonResponse({'message': {'text': '단편입니까?'},
                             'keyboard': {'type': 'button',
                                          'button': ['단편입니다', '장편입니다', '시리즈입니다']}})
    elif (return_str == '여행'):
        f.write('여행\n')
        return JsonResponse({'message': {'text': '단편입니까?'},
                             'keyboard': {'type': 'button',
                                          'button': ['단편입니다', '장편입니다', '시리즈입니다']}})
    elif (return_str == '자기계발'):
        f.write('자기계발\n')
        return JsonResponse({'message': {'text': '단편입니까?'},
                             'keyboard': {'type': 'button',
                                          'button': ['단편입니다', '장편입니다', '시리즈입니다']}})
    elif (return_str == '단편입니다' or return_str == '장편입니다' or return_str == '시리즈입니다'):
        return JsonResponse({'message': {'text': '가격대는 어느 정도를 생각하고 있습니까?'},
                             'keyboard': {'type': 'button',
                                          'button': ['10000 원 이내', '10000 원-30000 원', '30000 원 이상']}})
    elif (return_str == '10000 원 이내' or return_str == '10000 원-30000 원'
          or return_str == '30000 원 이상'):
        return JsonResponse({'message': {'text':'모든 질문에 응답을 마쳤습니다. \n결과를 보시겠습니까?'},
                             'keyboard': {'type': 'button',
                                          'button': ['결과를 보겠습니다', '다시 하겠습니다']}})
    elif (return_str == '다시 하겠습니다'):
        return JsonResponse({'message': {'text': 'PMB를 다시 시작하겠습니까?'},
                             'keyboard': {'type': 'button',
                                          'button': ['PMB 시작하기', '취소하겠습니다']}})
    elif (return_str == '결과를 보겠습니다'):
        f.close()
        f = open('result.txt', 'r+')
        details = f.readlines()
        details_index = random.randrange(0, len(details))

        txt_path = 'link\\%s.txt' %details[details_index][:-1]
        script_path = os.path.abspath(__file__)
        script_dir = os.path.split(script_path)[0]
        abs_txt_path = os.path.join(script_dir, txt_path)
        link = open(abs_txt_path, 'r+')
        link_lines = link.readlines()
        link_index = random.randrange(0, len(link_lines))
        return JsonResponse({'message': {'text': link_lines[link_index]},
                             'keyboard': {'type': 'button',
                                          'button': ['만족스러운 결과를 얻었습니다', '다시 하겠습니다']}})
    else:
        return JsonResponse({'message': {'text': 'PMB를 이용해 주셔서 감사합니다. \nPMB를 이용하고 싶으시면 PMB 시작하기 버튼을 눌러 주세요'},
                             'keyboard': {'type': 'button',
                                          'button': ['PMB 시작하기']}})