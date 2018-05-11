from django.db import models

# Create your models here.
from user.models import User
from goods.models import Goods
class Cart(models.Model):
    goods = models.ForeignKey(Goods,verbose_name='货物id',on_delete=models.CASCADE)
    cat_num = models.IntegerField(default=0, verbose_name='数量')
    user = models.ForeignKey(User,verbose_name='用户id',on_delete=models.CASCADE)
    count = models.CharField(max_length = 10,verbose_name='金额')

    def __str__(self):
        return str(self.id)
