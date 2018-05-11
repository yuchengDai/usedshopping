from django.db import models

# Create your models here.



class Category(models.Model):
    category_choices = (
        (0,u'手机通讯'),
        (1, u'平板电脑')
    )
    cate_type = models.IntegerField(choices=category_choices,verbose_name='商品分类')
    def __str__(self):
        return self.cate_type


class Brand(models.Model):
    brand_name = models.CharField(max_length=10,verbose_name='商品品牌名称')
    goods_type = models.CharField(max_length=20,null=True,verbose_name='商品型号')

    grade_choice = (
        (0, u's级'),
        (1, u'A级'),
        (2, u'B级'),
        (3, u'C级'),
    )
    brand_grade = models.IntegerField(choices=grade_choice,null=True,verbose_name='商品等级')

    size_choice = (
        (0, u'8G'),
        (1, u'16G'),
        (2, u'32G'),
        (3, u'64G'),
        (5, u'128G'),
        (6, u'256G'),
        (7, u'512G'),
    )
    brand_size = models.IntegerField(choices=size_choice,null=True,verbose_name='容量')

    net_choice = (
        (0, u'全网通'),
        (1, u'联通版'),
        (2, u'双4G'),
        (3, u'移动版'),
    )

    brand_net = models.IntegerField(choices=net_choice,null=True,verbose_name='商品网络')
    brand_color = models.CharField(max_length=10,null=True,verbose_name='商品颜色')
    category = models.ForeignKey(Category,verbose_name='对应的商品分类')
    def __str__(self):
        return self.brand_name



class Goods(models.Model):
    goods_name = models.CharField(max_length=10,verbose_name='商品名')
    goods_price = models.FloatField(default=0.0,verbose_name='商品价格')
    goods_num = models.PositiveIntegerField(default=0,verbose_name='商品数量')
    goods_info = models.CharField(max_length=255,verbose_name='商品描述')
    goods_pic = models.ImageField(upload_to='uploads/')
    brand = models.ForeignKey(Brand,verbose_name='商品对应的品牌规格')
    category = models.ForeignKey(Category,verbose_name='商品对应的分类')
    def __str__(self):
        return self.goods_name
