from django.db import models
from goods.models import Goods
from user.models import User

# Create your models here.
class Order(models.Model):
    order_num = models.CharField(max_length=20,verbose_name='订单号')
    order_many = models.FloatField(default=0.0,verbose_name='订单价格')
    order_many = models.CharField(max_length=10,verbose_name='收货人')
    order_site = models.CharField(max_length=30,verbose_name='收货地址')
    order_tel = models.CharField(max_length=11,verbose_name='收货电话')
    order_choice = (
        (0, u'未付款'),
        (1, u'已付款'),
    )
    order_status = models.IntegerField(choices=order_choice,verbose_name='订单状态')
    goods = models.ForeignKey(Goods,verbose_name='订单对应的商品ID')
    user = models.ForeignKey(User,verbose_name='订单对应的用户ID')
    def __str__(self):
        return self.order_num


