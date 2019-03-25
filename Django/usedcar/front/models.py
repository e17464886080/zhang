from django.db import models
from info.models import *
# Create your models here.
ORDERSTATUS=(
    (0,'已完成'),
    (1,'已支付'),
    (2,'交易关闭'),
    (3,'订单关闭'),
    (4,'交易中'),
)
class Order(models.Model):
    orderNo=models.CharField('订单号',max_length=100,db_index=True,unique=True)
    buy_user=models.ForeignKey(UserInfo,related_name='buser',verbose_name='买家')
    sale_user=models.ForeignKey(UserInfo,related_name='suser',verbose_name='卖家')
    car=models.CharField('车辆信息',max_length=200)
    price=models.DecimalField('价格',max_digits=8,decimal_places=2)
    date=models.DateTimeField('时间')
    orderStatus=models.IntegerField('订单状态',choices=ORDERSTATUS,default=0)
    idDel=models.BooleanField('是否删除',default=False)
    def __str__(self):
        return self.orderNo
    class Meta:
        db_table='Order'
        verbose_name='订单信息'
        verbose_name_plural=verbose_name