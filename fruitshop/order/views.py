from django.http import JsonResponse
from django.shortcuts import render

from cart.models import CarModel
from order.models import OrderModel, OrderGoodsModel
from utils.functions import get_order_num


def order(request):
    if request.method == 'GET':
        user = request.user
        carts = CarModel.objects.filter(user=user, is_select=True)
        # 订单号
        o_num = get_order_num()
        order = OrderModel.objects.create(user=user, o_num=o_num)
        for cart in carts:
            OrderGoodsModel.objects.create(order=order, goods=cart.goods, goods_num=cart.c_num)
        # 删除购物车中已经下单的商品信息
        carts.delete()
        order = OrderModel.objects.filter(user=user, o_num=o_num).first()
        order_info = OrderGoodsModel.objects.filter(order_id=order.id)
        return render(request, 'place_order.html', {'order_info': order_info})

#
# def order_info(request):
#     if request.method == 'GET':
#         order_id = request.GET.get('order_id')
#         order_info = OrderGoodsModel.objects.filter(order_id=order_id)
#         return render(request, 'place_order.html', {'order_info': order_info})





