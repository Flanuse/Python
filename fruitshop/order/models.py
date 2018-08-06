from django.db import models

from goods.models import GoodsInfo
from users.models import UserModel


class OrderModel(models.Model):
    user = models.ForeignKey(UserModel)
    o_num = models.CharField(max_length=64)  # 订单号
    # 0代表未付款，1代表已付款
    o_status = models.IntegerField(default=0)  # 状态
    o_create = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'order'


class OrderGoodsModel(models.Model):
    goods = models.ForeignKey(GoodsInfo)
    order = models.ForeignKey(OrderModel)  # 关联订单
    goods_num = models.IntegerField(default=1)  # 商品个数

    class Meta:
        db_table = 'order_goods'


