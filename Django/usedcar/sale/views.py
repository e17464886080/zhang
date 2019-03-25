import random

from django.shortcuts import render
# Create your views here.
from .models import *


def index(request):
    #1.查询被购买的以及为删除的车辆
    #2.调python的random()随机选择四个
    #3.返回
    car_list=CarInfo.objects.filter(isPurchase=False,idDel=False)
    car_four=random.sample(list(car_list),4)
    for ca in car_four:
        print(ca.serbran)
    return render(request,'index.html',locals())
def carinfo(request):
    return render(request,'info-message.html')

def detail(request):
    car_id=request.GET.get('car_id','')
    cat_id=int(car_id)
    carinfo=CarInfo.objects.filter(id=car_id).first()
    return  render(request,'detail.html',locals())