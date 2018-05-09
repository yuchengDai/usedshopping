from django.db import models

# Create your models here.
#分类表
class Category(models.Model):
    choices = (
        (0,'手机通讯'),
        (1, '平板电脑')
    )
    cate_type = models.IntegerField(choices=choices)




#品牌表
class Brand(models.Model):
    brand_name = models.CharField(max_length=10,verbose_name='商品品牌名称')
    brand_index = models.IntegerField(default=1, verbose_name='排列顺序')
    category = models.ForeignKey(Category)


#商品表
class Goods(models.Model):
    goods_name = models.CharField(max_length=10,verbose_name='商品名')
    goods_info = models.CharField(max_length=255,verbose_name='商品描述')
    goods_pic = models.ImageField(upload_to='uploads/')
    brand = models.ForeignKey(Brand)
