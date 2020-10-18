from django.shortcuts import render
from django.contrib.auth.models import auth
from django.http import HttpResponse
from django.http import JsonResponse

# Create your views here.
def index(request):
    return render(request, 'auction/index.html',{
    })

