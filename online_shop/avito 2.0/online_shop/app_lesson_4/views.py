from django.shortcuts import render
# Подключаем объект для выполнения HTTP-запроса
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('Домашка по 4 занятию')