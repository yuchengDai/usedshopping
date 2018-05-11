from django.db import models


# Create your models here.

class User(models.Model):
    user_name = models.CharField(max_length=20,verbose_name='用户名')
    user_password = models.CharField(max_length=60,verbose_name='用户密码')
    def __str__(self):
        return self.user_name

class UserAccount(models.Model):
    ushou = models.CharField(max_length = 500,default='',verbose_name='收获地址')
    uname = models.CharField(max_length = 50,default='',verbose_name='收货人')
    uphone = models.CharField(max_length = 11,default='',verbose_name='收货号码')

    upost = models.CharField(max_length = 6,default='',verbose_name='邮编')
    user = models.OneToOneField(User,default='')
    def __str__(self):
        return str(self.user_id)

