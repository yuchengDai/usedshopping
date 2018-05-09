from django.db import models

# Create your models here.
#订单表
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
    order_status = models.IntegerField(choices=order_choice)


