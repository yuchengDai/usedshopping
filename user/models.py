from django.db import models

# Create your models here.
#用户表
class User(models.Model):
    user_name = models.CharField(max_length=20,verbose_name='用户名')
    user_password = models.CharField(max_length=60,verbose_name='用户密码')
    user_tel = models.CharField(max_length=11,verbose_name='用户手机号')

#用户中心
class UserAccount(models.Model):
    ushou = models.CharField(max_length = 100,default='',verbose_name='收获地址')
    uname = models.CharField(max_length = 30,default='',verbose_name='收货人')
    uphone = models.CharField(max_length = 11,default='',verbose_name='收货号码')

    upost = models.CharField(max_length = 6,default='',verbose_name='邮编')
    user = models.OneToOneField(User)

