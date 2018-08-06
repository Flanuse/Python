from django.http import JsonResponse
from django.shortcuts import render

from cart.models import CarModel


def addtocart(request):
    if request.method == 'POST':
        user = request.user  # 没写中间件时，user是系统自带的user
        goods_id = request.POST.get('goods_id')
        data = {
            'code': 200,
            'msg': '请求成功'
        }
        if user.id:   # django自带的user没有user.id
            user_carts = CarModel.objects.filter(user=user, goods_id=goods_id).first()
            if user_carts:
                user_carts.c_num += 1
                user_carts.save()
                data['c_num'] = user_carts.c_num
            else:
                CarModel.objects.create(user=user, goods_id=goods_id)
                data['c_num'] = 1
            return JsonResponse(data)
        else:
            data['code'] = 403
            data['msg'] = '当前用户没有登录'
            return JsonResponse(data)


def subtocart(request):
    if request.method == 'POST':
        user = request.user
        goods_id = request.POST.get('goods_id')
        data = {
            'code': 200,
            'msg': '请求成功'
        }
        if user.id:
            user_cart = CarModel.objects.filter(user=user, goods_id=goods_id).first()
            if user_cart:
                if user_cart.c_num == 1:
                    user_cart.delete()
                    data['c_num'] = 0

                else:
                    user_cart.c_num -= 1
                    user_cart.save()
                    data['c_num'] = user_cart.c_num
                return JsonResponse(data)
            else:
                data['code'] = 300
                data['msg'] = '请添加商品'
                return JsonResponse(data)

        else:
            data['code'] = 400
            data['msg'] = '当前用户没有登录'
            return JsonResponse(data)


def goodsnum(request):
    if request.method == 'GET':
        user = request.user
        cart_list = []
        if user.id:
            carts = CarModel.objects.filter(user=user)
            for cart in carts:

                # price = int(cart.goods.price) * cart.c_num
                data = {
                    'id': cart.id,
                    'goods_id': cart.goods.id,
                    'c_num': cart.c_num,
                    'user_id': cart.user.id,
                    # 'price': price

                }
                cart_list.append(data)
            return JsonResponse({'carts': cart_list, 'code': 200})
        else:
            return JsonResponse({'carts': '', 'code': 1002})


def tocart(request):
    if request.method == 'GET':
        user = request.user
        carts = CarModel.objects.filter(user=user)
        return render(request, 'cart.html', {'carts': carts})


def totalprice(request):
    if request.method == 'GET':
        user = request.user
        carts1 = CarModel.objects.filter(user=user)
        price1_list = []
        for cart1 in carts1:
            price1 = int(cart1.goods.goodsprice) * cart1.c_num
            data = {

                'goods_id': cart1.goods.id,
                'c_num': cart1.c_num,
                'user_id': cart1.user.id,
                'price': price1,
                'is_select:': cart1.is_select
            }
            price1_list.append(data)
        carts = CarModel.objects.filter(user=user, is_select=True)
        total_price = 0
        price_list = []
        amount = 0
        for cart in carts:
            total_price += int(cart.goods.goodsprice) * cart.c_num
            amount += cart.c_num
            price = int(cart.goods.goodsprice) * cart.c_num
            data = {

                'goods_id': cart.goods.id,
                'c_num': cart.c_num,
                'user_id': cart.user.id,
                'price': price
            }
            price_list.append(data)
        return JsonResponse({'price1_list': price1_list, 'amount': amount, 'total_price': total_price, 'price_list': price_list, 'code': 200})


def deletegoods(request):
    if request.method == "GET":
        user = request.user
        goods_id = request.GET.get('goods_id')
        if user.id:
            CarModel.objects.filter(user=user, goods_id=goods_id).delete()
            data = {
                'code': 200,
                'msg': '请求成功'
            }
            return JsonResponse(data)
        else:
            data = {
                'code': 300,
                'msg': '该用户未登录'
            }
            return JsonResponse(data)


def changestatus(request):
    if request.method == 'POST':
        goods_id = request.POST.get('goods_id')
        cart = CarModel.objects.filter(goods_id=goods_id).first()
        if cart.is_select:
            cart.is_select = False
        else:
            cart.is_select = True
        cart.save()
        return JsonResponse({'code': 200, 'cart_is_select': cart.is_select})



