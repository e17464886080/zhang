import random
import logging
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse
from hashlib import md5
# Create your views here.
from django.shortcuts import render, redirect
from .models import *
from django.db import DatabaseError
from django.contrib.auth import authenticate, login, logout


def register(request):
    return render(request,'register.html')
def registerin(request):
    if request.method=="POST":
        #判断两次密码是否一直，将用户注册(加密注册)，返回
        #判断是否为post，判断用户，密码。判断用户是否存在，
        uname=request.POST.get('username','')
        pwd=request.POST.get('pwd','')
        upwd=request.POST.get('upwd','')
        if uname and pwd and upwd:
            if pwd!=upwd:
                user=UserInfo.objects.filter(username=uname)
                return render(request, 'register.html', {'msg': '两次密码不一致'})
            user=UserInfo.objects.filter(username=uname)
            if user:
                return render(request, 'register.html', {'msg': '用户已存在'})
            #参数1:加密密码,参数2:任意字符串,参数3:加密方式
            #得到的是遗传随机的字符串，每次都不一样
            newpwd=make_password(pwd,'pbkdf2_sha1')
            print(newpwd)
            try:
                user=UserInfo.objects.create(username=uname,password=newpwd)
            except DatabaseError as e:
                logging.warning(e)

            # ha=md5()
            # ha.update(pwd.encode())
            # pwd=ha.hexdigest()

            # user.save()
            return render(request,'register.html',{'msg':'注册成功'})
        else:
            return render(request,'register.html',{'msg':'帐号密码不能为空'})

def login_(request):
    return render(request,'login1.html')
def loginin(request):
    if request.method=='GET':
        #获取用户名和密码,验证
        #存session,使用django自带的登录
        name=request.GET.get('username','')
        pwd=request.GET.get('userpwd','')
        if name and pwd:
            newpwd=make_password(pwd,'pbkdf2_sha1')
            #使用django提供的验证方法,传入用户名和密码,返回一个user对象
            user=authenticate(username=name,password=pwd)
            if user is not None and user.is_active:
                #登录
                login(request,user)
                return redirect('/',{'msg':'登录成功'})
                pass
            else:
                return render(request,'login1.html',{'msg':'用户名或密码错误'})
            resp=redirect('/user/index/')
            # user=UserInfo.objects.filter(username=name)
            # if not user:
            #     return render(request,'login1.html',{'msg':'该用户未注册'})
            # else :
            #     if newpwd==user.password:
            #         #check_paddword(明文,密文)
            #         return render(request,'login1.html',{'msg':'登录成功'})
            #     else:
            #         return render(request,'login1.html',{'msg':'登录失败'})
        else:
            return render(request, 'login1.html', {'msg': '该项不能为空'})
def detail(request):
    return render(request,'detail.html')
def header(request):
    return render(request,'header.html')
def logout_(request):
    logout(request)
    return redirect('/')