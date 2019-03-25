from django.contrib.auth.models import AbstractUser
from django.db import models
SEX_CHOICES={
    (1,'男'),
    (0,'女')
}
CARDTYPE=(
    (0,'储蓄卡'),
    (1,'信用卡'),
    (0,''),
)
BANK=(
    (0,'中国建设银行'),
    (1,'中国农业银行'),
    (2,'中国邮政储蓄'),
    (2,'中国'),
)
CARDSTATUS=(
    (0,''),
    (0,''),
    (0,''),
    (0,''),
)
# Create your models here.
class UserInfo(AbstractUser):
    age=models.IntegerField('年龄',null=True,blank=True)
    sex=models.IntegerField('性别',choices=SEX_CHOICES,default=1)
    cellphone=models.CharField('手机号',max_length=11,null=True,blank=True,unique=True)
    idcard=models.CharField('身份证',max_length=20,null=True,blank=True)
    address=models.CharField('地址',max_length=100,null=True,blank=True)
    def __str__(self):
        return self.username
    class Meta:
        db_table='Users'
        verbose_name='用户信息表'
        verbose_name_plural=verbose_name

class bankcard(models.Model):
    cardID=models.CharField('卡号',max_length=30)
    username=models.CharField('开户名',max_length=20)
    type=models.IntegerField('类型',choices=CARDTYPE)
    bank=models.IntegerField('开户行',choices=BANK)
    cardStatus=models.IntegerField('状态',choices=CARDSTATUS)
    user=models.ForeignKey(UserInfo,related_name='bankcard')
    def __str__(self):
        return self.cardID
    class Meta:
        db_table='银行卡'
        verbose_name='bankcard'
        verbose_name_plural=verbose_name

