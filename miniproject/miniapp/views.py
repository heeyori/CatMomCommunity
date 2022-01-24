from turtle import st
from aiohttp import request
from django.shortcuts import redirect,render
from django.http import HttpResponse,JsonResponse
from .models import User,Img,Cat
from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

def login(request):
    return render(request, 'miniapp/login.html' )

def signup(request):
    if request.method == 'POST':
        user_id = request.POST.get('id')
        user_pw = request.POST.get('password1')
        user_name = request.POST.get('username')
        user_email = request.POST.get('email')
        user_nickname = request.POST.get('nickname')
        user_bitrh =request.POST.get('birth')
        m = User(
            user_id=user_id, user_pw=user_pw, user_name=user_name,user_email=user_email, user_nickname=user_nickname, user_bitrh=user_bitrh)
        m.date_joined = timezone.now()
        m.save()
        return render(request, 'miniapp/signup_complete.html' )
    else:
        return render(request, 'miniapp/signup.html' )

def signup_complete(request):
    return render(request, 'miniapp/signup_complete.html' )

def upload_cat_img(request):
    if request.method == 'POST':
        img = request.FILES.get('img-file')
        Img.objects.create(img=img)
        return redirect(upload_cat_img)
    else:
        img = Img.objects.all()
    context = {
        'object': img
    }
    return render(request, 'miniapp/upload_cat_img.html', context)


def show(request):
    img = Img.objects.all()
    context = {
        'object': img
    }
    return render(request, 'miniapp/show.html', context)
def create_cat(request):
    if request.method == 'POST':
        cat_name = request.POST.get('cat_name')
        gender = request.POST.get('gender')
        neutral = request.POST.get('neutral')
        location1 = request.POST.get('location1')
        location2 = request.POST.get('location2')
        location3 =request.POST.get('location3')
        appearance = request.POST.get('흰색')
        status =request.POST.get('status')
        m = Cat(
            cat_name=cat_name, gender=gender, neutral=neutral,location1=location1, location2=location2, location3=location3, appearance=appearance, status=status)
        m.save()
    return render(request, 'miniapp/create_cat.html')

