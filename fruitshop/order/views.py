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
        # carts.delete()
        order = OrderModel.objects.filter(user=user, o_num=o_num).first()
        order_info = OrderGoodsModel.objects.filter(order_id=order.id)
        return render(request, 'place_order.html', {'order_info': order_info})


def orderchange(request):
    if request.method == 'POST':
        user = request.user
        carts = CarModel.objects.filter(user=user, is_select=True)
        carts.delete()
        order_id = request.POST.get('order_id')
        order = OrderModel.objects.get(id=order_id)
        order.o_status = 1
        order.save()
        return JsonResponse({'code': 200})


def amountprice(request):
    if request.method == 'GET':
        user = request.user
        orders = OrderModel.objects.filter(user=user, o_status=0)
        for order in orders:
            order_infos = OrderGoodsModel.objects.filter(order_id=order.id)
            amount = 0
            price_list = []
            for order_info in order_infos:
                price = order_info.goods_num * int(order_info.goods.goodsprice)
                amount += price
                data = {
                    'order_id': order_info.id,
                    'price': price
                }
                price_list.append(data)
        return JsonResponse({'amount': amount, 'price_list': price_list, 'code': 200})

        # orders1 = OrderModel.objects.filter(user=user, o_status=1)
        # for order1 in orders1:
        #     order1_infos = OrderGoodsModel.objects.filter(order_id=order1.id)
        #     amountpr = 0
        #     price_list1 = []
        #     for order1_info in order1_infos:
        #         price1 = order1_info.goods_num * int(order1_info.goods.goodsprice)
        #         amountpr += price1
        #         data = {
        #             'order_id': order1_info.id,
        #             'price1': price1
        #         }
        #         price_list1.append(data)


