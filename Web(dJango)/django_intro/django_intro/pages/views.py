from django.shortcuts import render
import random

# Create your views here.

def index(request):
    return render(request, 'index.html')



def dinner(request):
    menu = ['순대국밥', '쌀국수', '햄버거', '곱창']
    choice = random.choice(menu)

    return render(request, 'dinner.html', {'dinner': choice})


def greeting(request, name):
    return render(request,'greeting.html', {'name': name})