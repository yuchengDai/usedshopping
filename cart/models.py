from django.db import models

# Create your models here.
#购物车
from goods.models import Goods
from user.models import User


class Cart(models.Model):
    goods = models.ForeignKey(Goods,verbose_name='货物id',on_delete=models.CASCADE)
    user = models.OneToOneField(User,verbose_name='用户id')
