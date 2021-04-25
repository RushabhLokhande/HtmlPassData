from django.http import HttpResponse
from django.shortcuts import render

def index(request):
 values = {'name':'prince', 'age':20, 'city':'pune'}
 return render(request, 'home.html', values)