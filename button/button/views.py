from django.shortcuts import render
from subprocess import run, PIPE
import sys
import requests


def button(request):
    return render(request, 'home.html')


def external(request):
    run([sys.executable,'C://Users//Hp//PycharmProjects//GestureRecoginition_SignLanguage//test.py'], shell=False,stdout=PIPE)

    return render(request, 'home.html')
