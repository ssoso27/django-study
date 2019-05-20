from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
import random

# Create your views here.
def index(request):
    # return HttpResponse("hi?")
    return render(request, 'home/index.html')
    
def lotto(request):
    numbers = range(1, 46)
    lottos = random.sample(numbers, 6)
    real_lottos = [3, 5, 12, 24, 30, 41]
    contents = { 
        "real_lottos" : real_lottos, 
        "lottos" : lottos
    }
    return render(request, 'home/lotto.html', contents)
    # return HttpResponse(lottos)
    
def halo(request):
    return render(request, 'home/halo.html')
    
def dinner(request):
    menus = ['pizza', 'bob', 'chicken']
    picked = random.choice(menus)
    return render(request, 'home/dinner.html', {'menus' : menus, 'picked' : picked})
    
def midnight(request):
    menus = ['chocolate', 'candy', 'icecream', 'snack']
    picked = random.choice(menus)
    context = {
        "menus" : menus,
        "picked" : picked
    }
    return render(request, 'home/midnight.html', context)
    
def hello(request, name):
    return render(request, 'home/hello.html', {'name' : name})
    
def cube(request, num):
    nums = num ** 3
    return render(request, 'cube.html', {'num' : num, 'nums' : nums})
    
# 이름과 나이를 받고, 
# template에서 (name)의 나이는 (age) 입니다. 라고 보여줘라.
def introduce(request, name, age):
    contents = {
        "name" : name,
        "age" : age
    }
    return render(request, 'home/introduce.html', contents)

def times(request, num1, num2) :
    num3 = num1 * num2
    contents = {
        "num1" : num1,
        "num2" : num2,
        "num3" : num3
    }
    return render(request, 'home/times.html', contents)
    
def area(request, r):
    result = r * r * 3.14
    contents = {
        "r" : r,
        "result" : result,
    }
    return render(request, 'home/area.html', contents)
    
# 오늘이 내 생일이면 예, 아니면 아니오 출력
# datetime 모듈
def isbirth(request):
    today = datetime.now()
    
    result = False
    if today.month == 8 and today.day == 29:
        result = True
    
    contents = {
        "today" : today,
        "result" : result
    }
    
    return render(request, "home/isbirth.html", contents)
    
def template_example(request):
    chiness_foods = ['짜장면', '탕수육', '짬뽕', '양장피']
    fruits = ['apple', 'banana', 'cucumber', 'mango', 'watermelon']
    empty_list = []
    
    contents = {
        "chiness_foods" : chiness_foods,
        "fruits" : fruits,
        "empty_list" : empty_list
    }
    
    return render(request, "home/template_example.html", contents)
    
def ping(request):
    return render(request, "home/ping.html")
    
def pong(request):
    data = request.GET.get('data')
    return render(request, "home/pong.html", {'data' : data})
    
def static_example(request):
    return render(request, "home/static_example.html")