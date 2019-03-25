from django.db import models
from info.models import *
# Create your models here.
EXAMINE=(
    (0,'审核中'),
    (1,'审核通过'),
    (2,'审核不通过'),
)
class Brand(models.Model):
    btitle=models.CharField(max_length=30,verbose_name='汽车品牌')
    type=models.CharField(max_length=50)
    logo=models.ImageField(upload_to='static/images',null=True,verbose_name='logo')
    is_del=models.BooleanField('是否删除',default=False)
    def __str__(self):
        return self.btitle
    class Meta:
        db_table='Brand'
        verbose_name='品牌表'
        verbose_name_plural=verbose_name

class CarInfo(models.Model):
    serbran=models.ForeignKey(Brand,related_name='carinfo')
    mileage=models.IntegerField('公里数',default=0)
    maintenance=models.BooleanField(default=False,verbose_name='维修记录')
    year=models.CharField(max_length=30,verbose_name='年份')
    color=models.CharField(max_length=30,verbose_name='颜色')
    picture=models.ImageField(upload_toee='eeestatic/images',verbose_name='图片')
    num=models.DecimalField(max_digits=2,decimal_places=1,verbose_name='排量')
    price=models.DecimalField(max_digits=4,decimal_places=0,verbosee_name='价格')
    user=models.ForeignKey(UserInfo,verbose_name='卖家e')
    isPurchase=models.BooleanField(default=True,verbose_name='是否购买')
    formalitiles=models.BooleanField(default=False,verbose_name='手续是否齐全')
    debt=models.BooleanField(default=False,verbose_name='是否有债务')
    regist=models.DateField(verbose_name='上牌日期')
    engineNo=models.CharField(max_length=30,verbose_name='发动机号')
    examine=models.IntegerField(choices=EXAMINE,default=0,verbose_name='审核进度')
    ctitle=models.CharField(max_length=30,verbose_name='车名')
    newprice=models.DecimalField(max_digits=4,decimal_places=0,verbose_name='新车价格')
    idDel=models.BooleanField(default=False)
    def __str__(self):
        return str(self.serbran)
    class Meta:
        db_table='CarInfo'
        verbose_name='车辆信息'
        verbose_name_plural=verbose_name