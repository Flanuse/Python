from django.db import models


# 商品类型
class TypeInfo(models.Model):
    typename = models.CharField(max_length=30)
    isDelete = models.BooleanField(default=False)

    class Meta:
        db_table = 'typeinfo'


class GoodsInfo(models.Model):
    goodsname = models.CharField(max_length=30, unique=True)
    goodsid = models.CharField(max_length=10, unique=True, null=False, default='')
    goodspic = models.CharField(max_length=255, null=True)
    goodsprice = models.CharField(max_length=10)
    isDelete = models.BooleanField(default=False)
    goodsunit = models.CharField(max_length=20, default='克')  # 单位
    goodsclick = models.CharField(max_length=10, default='')  # 点击
    gjianjie = models.CharField(max_length=200, default='')
    gkucun = models.CharField(max_length=10, default='')
    gcontent = models.CharField(max_length=200, default='')
    gtype = models.ForeignKey(TypeInfo)  # 外键

    class Meta:
        db_table = 'goodsinfo'
